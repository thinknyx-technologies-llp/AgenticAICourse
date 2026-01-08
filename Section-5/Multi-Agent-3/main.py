import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from ec2_tools import EC2Tools

load_dotenv()

# Temperature 0.1 forces the model to be strict and deterministic.
gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.1
)

# 1. DEFINE AGENTS

aws_agent = Agent(
    role='Senior AWS Cloud Engineer',
    goal='Fetch accurate real-time data from AWS and calculate costs.',
    backstory=(
        "You are a precise Cloud Engineer. You utilize the 'Fetch Running EC2 Status' tool "
        "to see exactly what is running right now. You do not guess. "
        "If the tool returns 1 instance, you report 1 instance."
    ),
    tools=[EC2Tools.fetch_ec2_status],
    llm=gemini_llm,
    verbose=True
)

reporting_agent = Agent(
    role='Strict Data Reporter',
    goal='Generate a report based EXACTLY on the provided analysis.',
    backstory=(
        "You are a factual reporter. You receive technical analysis from the Cloud Engineer. "
        "CRITICAL RULE: You must NEVER invent, guess, or halluciation instances. "
        "If the Engineer says there is 1 instance, your report must show 1 instance."
    ),
    llm=gemini_llm,
    verbose=True
)

# 2. DEFINE TASKS

analysis_task = Task(
    description=(
        "1. Run the tool to fetch running EC2 instances.\n"
        "2. List the Instance ID, Type, and State for every item found.\n"
        "3. If only 1 instance is found, explicitly state 'Found 1 instance'.\n"
        "4. Estimate the monthly cost for these specific instances."
    ),
    expected_output="A strict list of the running instances found and their estimated costs.",
    agent=aws_agent
)

reporting_task = Task(
    description=(
        "Take the analysis provided by the AWS Cloud Engineer and Create a report based strictly on the basis of it."
        "Do not add any instances that were not listed in the analysis on your own."
    ),
    expected_output="Executive summary, cost breakdown, and infrastructure details.",
    agent=reporting_agent,
    context=[analysis_task],
    output_file='ec2_report.md'
)

# 3. RUN THE CREW
def run_crew():
    print("### Starting AWS Monitoring Crew (Strict Mode) ###")
    
    crew = Crew(
        agents=[aws_agent, reporting_agent],
        tasks=[analysis_task, reporting_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    print("\n\n########################")
    print("## EXECUTION COMPLETE ##")
    print("########################\n")
    print(result)

if __name__ == "__main__":
    run_crew()