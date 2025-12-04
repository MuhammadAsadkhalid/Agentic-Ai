from agents import Agent, Runner
from dotenv import load_dotenv
import os

load_dotenv()

# Make sure GEMINI_API_KEY is set in .env
agent = Agent(
    name="Doctor",
    instructions="You are a medical assistant.",
    tools=[],
    model="gemini-2.5-flash"
)

response = Runner.run_sync(agent, "What is the reason behind fever?")

print(response.output)
