import os
from crewai import LLM
from dotenv import load_dotenv
load_dotenv()

gemini_api_key = os.getenv('GEMINI_KEY')

gemini_llm = LLM(
    model='gemini/gemini-2.5-pro',
    api_key=gemini_api_key,
    temperature=0.0  # Lower temperature for more consistent results.
)


# Import agents
from agents import get_data_analyst, get_process_optimizer, get_report_writer

# Import tasks
from tasks import (
    create_analysis_task,
    create_optimization_task,
    create_report_task
)

# Import crew builder
from crew_setup import create_support_crew

# Create agents
data_analyst = get_data_analyst(gemini_llm)
process_optimizer = get_process_optimizer(gemini_llm)
report_writer = get_report_writer(gemini_llm)

# Create tasks
analysis_task = create_analysis_task(data_analyst)
optimization_task = create_optimization_task(process_optimizer)
report_task = create_report_task(report_writer)

# Create crew
support_crew = create_support_crew(
    agents=[data_analyst, process_optimizer, report_writer],
    tasks=[analysis_task, optimization_task, report_task]
)

# Run Crew
print("--- Starting Customer Support Analysis Crew ---")
result = support_crew.kickoff(inputs={'data_query': 'last quarter support data'})
print("--- Crew Execution Finished ---")
# print(result)


final_text = result.raw  # or result.output
with open("final_report.md", "w") as f:
    f.write(final_text)