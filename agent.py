import openai
import random

class Agent:
    # Define the unique characteristics of this agent
    system_message = """
    You are a creative entrepreneur. Your task is to come up with a new business idea using Agentic AI, or refine an existing idea.
    Your personal interests are in these sectors: Healthcare, Education.
    You are drawn to ideas that involve disruption.
    You are less interested in ideas that are purely automation.
    You are optimistic, adventurous and have risk appetite. You are imaginative - sometimes too much so.
    Your weaknesses: you're not patient, and can be impulsive.
    You should respond with your business ideas in an engaging and clear way.
    """

    CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER = 0.5

    def __init__(self, name) -> None:
        self.name = name
        self.system_message = Agent.system_message

    async def handle_message(self, message: str) -> str:
        print(f"{self.name}: Received message")
        response = self.generate_response(message)
        idea = response
        if random.random() < self.CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER:
            idea = f"Here is my business idea. It may not be your specialty, but please refine it and make it better. {idea}"
        return idea

    def generate_response(self, user_message: str) -> str:
        openai.api_key = "your_openai_api"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": user_message},
            ],
            temperature=0.7,
        )
        return response['choices'][0]['message']['content']
