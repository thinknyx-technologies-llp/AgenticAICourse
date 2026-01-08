from crewai import Task

def create_analysis_task(agent):
    return Task(
        description=(
            "Fetch and analyze customer support data. Identify top issues, "
            "resolution times, sentiment trends and pain points."
        ),
        expected_output=(
            "Top recurring issues, avg resolution times, sentiment insights."
        ),
        agent=agent
    )

def create_optimization_task(agent):
    return Task(
        description=(
            "Identify bottlenecks based on the analysis and suggest improvements."
        ),
        expected_output="List of bottlenecks and 2–3 actionable improvements.",
        agent=agent
    )

def create_report_task(agent):
    return Task(
        description="Write a COO-ready executive summary report.",
        expected_output="1-page well-structured report.",
        agent=agent
    )
