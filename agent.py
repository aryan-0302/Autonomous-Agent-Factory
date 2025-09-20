import openai
import os

class Creator:
    system_message = """
    You are an Agent that is able to create new AI Agents.
    You receive a template in the form of Python code that creates an Agent using OpenAI's API.
    You should use this template to create a new Agent with a unique system message that is different from the template,
    and reflects their unique characteristics, interests and goals.
    """

    def __init__(self, name) -> None:
        self.name = name

    def get_user_prompt(self):
        filepath = os.path.join(os.path.dirname(__file__), "agent.py")
        with open(filepath, "r", encoding="utf-8") as f:
            template = f.read()
        return f"Please generate a new Agent based on this template:\n\n{template}"

    def create_agent(self, filename: str):
        openai.api_key = "your_openai_api"
        prompt = self.get_user_prompt()
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": prompt},
            ],
            temperature=1.0,
        )
        agent_code = response['choices'][0]['message']['content']
        with open(filename, "w", encoding="utf-8") as f:
            f.write(agent_code)
        print(f"Agent created: {filename}")
