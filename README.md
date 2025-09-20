# Autonomous Agent Factory

The **Autonomous Agent Factory** is a Python-based project that creates and manages multiple autonomous AI agents. These agents are designed to generate and refine business ideas based on their unique characteristics, interests, and goals. The project leverages OpenAI's GPT model to simulate brainstorming and collaboration between agents.

---

## Features

- **Dynamic Agent Creation**: A `Creator` agent generates new agents dynamically using a Python template.
- **Unique Agent Personalities**: Each agent has a unique system message that defines its personality, interests, and goals.
- **Business Idea Generation**: Agents generate creative business ideas based on their system message.
- **Collaboration**: Agents can refine their ideas by "bouncing" them off other agents.
- **Scalable**: The system can create and manage multiple agents concurrently.

---

## How It Works

1. **Entry Point**:
   - The `world.py` script is the entry point of the system.
   - It initializes a `Creator` agent and uses it to generate multiple agents.

2. **Agent Creation**:
   - The `Creator` agent reads the `agent.py` file as a template.
   - It modifies the template to create new agents with unique system messages.
   - The generated agents are saved as Python files (e.g., `agent1.py`, `agent2.py`, etc.).

3. **Idea Generation**:
   - Each agent generates a business idea based on its system message and the input prompt.
   - The generated ideas are saved as Markdown files (e.g., `idea1.md`, `idea2.md`, etc.).

4. **Collaboration**:
   - Agents may refine their ideas by collaborating with other agents (probabilistically).

---

## Project Structure
