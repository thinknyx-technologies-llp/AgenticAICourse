from crewai import Agent
from tools import CustomerSupportDataTool

support_tool = CustomerSupportDataTool()

def get_data_analyst(llm):
    return Agent(
        role="Customer Support Data Analyst",
        goal="Analyze customer support interactions and identify patterns.",
        backstory="You specialize in support data analysis.",
        verbose=True,
        tools=[support_tool],
        llm=llm
    )

def get_process_optimizer(llm):
    return Agent(
        role="Process Optimization Specialist",
        goal="Identify bottlenecks and suggest improvements.",
        backstory="You optimize workflows and reduce resolution delays.",
        verbose=True,
        llm=llm
    )

def get_report_writer(llm):
    return Agent(
        role="Executive Report Writer",
        goal="Create a clear, concise COO-ready report.",
        backstory="You excel in transforming analysis into business insights.",
        verbose=True,
        llm=llm
    )
