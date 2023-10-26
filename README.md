# Cogs: Your Open-source Agent Creation Framework

Cogs is a dynamic open-source framework that empowers developers, data scientists, and AI enthusiasts to construct and evolve intelligent agents seamlessly. "Cogs" comes from a combination of cognitive processes and the cogs of a machine. Instead of chains, we see agents being a combination of cognitive processes working towards a goal. Each cognitive process can be executed with an LLM e.g. ONE instance of OpenAI's ChatGPT chat, primed by a prompt for that cognitive process. The simplest Cogs agent will have two processes (and prompts) - ONE for interacting with the user, ONE for reflection and improving the prompt, such that the next time the agent runs, it will interact with the user with the improved prompt.

## Core Features

### Adaptive Learning
Cogs agents are designed to learn and adapt. Following every interaction, users have the opportunity to provide feedback and modify the agent’s instructions. This iterative feedback loop ensures continuous learning and refinement, enhancing the agent’s performance over time.

### Open-Source Collaboration
Cogs thrives on the collective intelligence of a global community of developers. We welcome contributions, enhancements, and innovations from all, to make Cogs a robust, versatile, and user-friendly framework.

## Getting Started with Cogs
Embark on your journey to create intelligent, responsive agents by cloning or forking the Cogs repository. Follow the detailed instructions to set up and customize your agent.

### Install Requirements
Ensure you have all the necessary packages installed to run your agent seamlessly.
```
pip install -r agent/requirements.txt
```

### Set Environment Variables
```
OPENAI_API_KEY=<YOUR KEY HERE>
```

### Run Your Agent
Initiate a conversation with your agent and begin the interactive experience.
```
python agent/chat.py
```

## Contribute to Cogs’ Growth
Join us in enhancing and expanding the Cogs ecosystem. Your insights, skills, and contributions are invaluable. 

### Future

#### Creating New Agents
While Cogs is perfectly suited for creating individual agents, it's designed with scalability in mind. We are actively working to enhance the framework's capability to support the development and management of multiple agents simultaneously, promoting efficiency and consistency.

#### Add Functions 
Add support for functions and python code generation so that it can actually improve. 

### Issue Resolution
Explore the existing issues in the repository, and if you possess solutions or enhancements, we encourage you to fork the repo, implement your updates, and rigorously test the code.

### Pull Requests
Once confident in your contributions, initiate a pull request. Remember, the primary Cogs repository is a seed for new agents, devoid of specific purposes, ensuring versatility and adaptability for diverse applications.

### Community Engagement
Connect with a vibrant community of developers and AI enthusiasts. Share your insights, seek assistance, and collaborate on projects to push the boundaries of what Cogs can achieve.

### Pro-tip:
Use Github codespaces!

We are excited about the limitless possibilities that Cogs offers and are eager to witness the innovative applications and enhancements that the community will bring. Join us in shaping the future of interactive, adaptive, and intelligent agent technology!

### Disclaimer: Regarding Involvement of AI Hero
While AI Hero is committed to keeping this Open Source, AI Hero wants to use this project as a means of "Research in Public" - we want to figure out how agents can be created, instructed, and run. With that in mind, we might use insert some OPTIONAL code hooked to AI Hero services so that the system can be improved. For example, we will be adding prompt versioning and tracking, to this using PromptStash and PromptCraft.

** No data will be sent to AI Hero if you don't set the env vars for it **
