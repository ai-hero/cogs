import openai
import os
import dotenv
from skills.db import SkillsDB
import json
import time
def load_prompt():
    """Load the prompt"""
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instructions.prompt')):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instructions.prompt'), 'r', encoding="utf-8") as file:
            return file.read().strip()
    elif os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'purpose.prompt')):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'purpose.prompt'), 'r', encoding="utf-8") as file:
            return file.read().strip()
    else:
        raise FileNotFoundError("Neither agent.prompt nor purpose.prompt found!")

def chat(prompt, skills_db):
    """Chat with the user"""
    print("You are now chatting with the agent. Type END to end the conversation.")
    messages = [{'role': 'system', 'content': prompt}]
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
    print("Agent:", response['choices'][0]['message']['content'].strip())
    messages.append(response['choices'][0]['message'])
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == 'end':
            break
        tic = time.perf_counter()
        messages.append({'role': 'user', 'content': user_input})
        relevant_skills = skills_db.search(user_input)
        if len(relevant_skills) > 0:
            if will_it_help(user_input, relevant_skills[0]['description']):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    functions=relevant_skills
                )
                if response['choices'][0]['message']['role'] == 'assistant' and response['choices'][0]['message']['content'] is None:
                    to_call = response['choices'][0]['message']["function_call"]
                    resp = skills_db.execute_command(to_call['name'], json.loads(to_call['arguments']))
                    messages.append( # adding function response to messages
                        {
                            "role": "function",
                            "name": to_call['name'],
                            "content": f"{resp}",
                        }
                    ) 
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=messages,
                    )
                    print("Agent (using skills):", response['choices'][0]['message']['content'].strip())
                else:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=messages,
                    )
                    print("Agent (no matching skills):", response['choices'][0]['message']['content'].strip())
            else:
                response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=messages,
                    )
                print("Agent (no known skills):", response['choices'][0]['message']['content'].strip())

        else:
            print("Agent:", response['choices'][0]['message']['content'].strip())
        toc = time.perf_counter()
        print(f"\t\t\t\t({toc - tic:0.4f}s)")
        messages.append(response['choices'][0]['message'])

    return "\n".join([f"{message['role']}: {message['content']}\n" for message in messages])


def collect_feedback():
    """Collect user feedback"""
    print("\nPlease provide feedback pointing to specific example where the agent went wrong.")
    feedback = input("Feedback: ")
    return feedback

def update_prompt(prompt, conversation, feedback):
    """Update the prompt for the agent."""
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reflect.prompt')):
        while True:  # Loop to continuously improve the prompt based on user feedback
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reflect.prompt'), 'r', encoding="utf-8") as file:
                reflect_prompt = file.read().strip()

            messages = [
                {'role': 'system', 'content': reflect_prompt},
                {'role': 'user', 'content': f"Original Instructions:\n{prompt}\nLast Conversation:\n{conversation}\nFeedback:\n{feedback}"}
            ]
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            
            new_prompt = response['choices'][0]['message']['content'].strip()
            print("\nNew Prompt:", new_prompt)

            # Ask the user for confirmation or additional feedback
            user_input = input("Is this new prompt up to your liking? (yes/no): ").strip().lower()
            if user_input.lower() == 'yes':
                with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instructions.prompt'), 'w', encoding="utf-8") as file:
                    file.write(new_prompt)
                    print("The instructions.prompt file has been updated.")
                break  # Exit the loop if the user is satisfied
            elif user_input.lower() == 'no':
                feedback = input("Please provide additional feedback to refine the prompt: ").strip()
                # Loop will continue with the new feedback
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
    else:
        print("Reflect prompt file not found.")

def will_it_help(question, function_description):
    messages = [{'role': 'user', 'content': f"Will the python function '{function_description}' help me with '{question}'?"}]
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
    return 'yes' in response['choices'][0]['message']['content'].lower()

def main():
    """Main loop`"""
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')):
        print("Loading .env file")
        dotenv.load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'))

    # Replace with your OpenAI API key
    openai.api_key = os.environ["OPENAI_API_KEY"]
    skills_db = SkillsDB()
    
    prompt = load_prompt()
    conversation = chat(prompt, skills_db)
    feedback = collect_feedback()
    update_prompt(prompt, conversation, feedback)

if __name__ == "__main__":
    main()
