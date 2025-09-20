import asyncio
from agent import Agent
from creator import Creator

HOW_MANY_AGENTS = 20

async def create_and_message(creator: Creator, i: int):
    try:
        # Generate a new agent file using the Creator agent
        agent_filename = f"agent{i}.py"
        creator.create_agent(agent_filename)

        # Simulate the agent generating a business idea
        agent = Agent(name=f"Agent{i}")
        idea = await agent.handle_message("Generate a business idea.")
        
        # Save the idea to a Markdown file
        with open(f"idea{i}.md", "w") as f:
            f.write(idea)
        print(f"Agent {i} created and idea saved to idea{i}.md")
    except Exception as e:
        print(f"Failed to create agent {i} due to exception: {e}")

async def main():
    # Initialize the Creator agent
    creator = Creator(name="Creator")

    # Create agents and generate ideas concurrently
    coroutines = [create_and_message(creator, i) for i in range(1, HOW_MANY_AGENTS + 1)]
    await asyncio.gather(*coroutines)

if __name__ == "__main__":
    asyncio.run(main())
