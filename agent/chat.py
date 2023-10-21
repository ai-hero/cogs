import openai
import os

# Replace with your OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

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

def chat(prompt):
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
        if user_input.strip().upper() == 'END':
            break
            
        messages.append({'role': 'user', 'content': user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        print("Agent:", response['choices'][0]['message']['content'].strip())
        messages.append(response['choices'][0]['message'])

    return "\n".join([f"{message['role']}: {message['content']}\n" for message in messages])


def collect_feedback():
    """Collect user feedback"""
    print("\nPlease provide feedback pointing to specific example where the agent went wrong.")
    feedback = input("Feedback: ")
    return feedback

def update_prompt(prompt, conversation, feedback):
    """Update the prompt with for the agent."""
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reflect.prompt')):
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

        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instructions.prompt'), 'w', encoding="utf-8") as file:
            file.write(new_prompt)
            print("The instructions.prompt file has been updated.")
    else:
        print("Reflect prompt file not found.")

def main():
    """Main loop`"""
    prompt = load_prompt()
    conversation = chat(prompt)
    feedback = collect_feedback()
    update_prompt(prompt, conversation, feedback)

if __name__ == "__main__":
    main()
