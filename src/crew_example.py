from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

researcher = Agent(
    role="Research",
    goal="Research new AI insights",
    backstory="You are a researcher at a top AI lab",
    verbose=True,
    allow_delegation=False,
)

writer = Agent(
    role="Writer",
    goal="Write a compelling and engaging blog posts about AI trends and insights",
    backstory="You are a writer at a top AI blog",
    verbose=True,
    allow_delegation=False,
)

task1 = Task(description="Research the latest AI trends", agent=researcher)
task2 = Task(
    description="Write a compelling blog post about the latest AI trends",
    agent=writer,
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=2,
    process=Process.sequential,
)

result = crew.kickoff()
