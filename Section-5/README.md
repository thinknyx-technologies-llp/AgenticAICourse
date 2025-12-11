## Section 5

---

## Project 9 – Demonstration: Building a Simple Multi-Agent System using CrewAI

### Project Description
This project introduces the fundamental concepts of multi-agent orchestration using **CrewAI**, a powerful framework for defining and managing collaborative AI teams. The demonstration builds a simple yet effective two-agent system powered by **Google Gemini** and equipped with external web-searching capabilities via the **Serper Dev Tool** (also referred to as SuperDev Tool).

The system's goal is to research a topic and produce a clean, beginner-friendly markdown report.

The two agents are:
1.  **Research Agent (The Detective)**: Its role is to use the **Serper Dev Tool** to perform real-time web searches, gather insights, and compile a detailed, bullet-point search summary on the given topic.
2.  **Writer Agent (The Editor)**: Its role is to receive the raw summary from the Research Agent and transform it into a polished, clear, and well-structured explanation for beginners.

The project highlights how CrewAI acts as the **orchestrator**, connecting the agents, assigning their respective tasks, and ensuring the seamless flow of information from the researcher to the writer to achieve the final deliverable.

### Flow Diagram
<img width="852" height="468" alt="Simple Multi-Agent System " src="https://github.com/user-attachments/assets/ef1936d9-185f-4620-be41-e3726e05d438" />



## Project 10 – Customer Support Analysis Crew using CrewAI (Custom Tools & Sequential Flow)

### Project Description
This demonstration focuses on building a sophisticated, production-ready Multi-Agent System (MAS) using the CrewAI framework to tackle a real-world business problem: analyzing customer support data. The system employs three specialized, cooperating agents in a **strictly sequential flow** orchestrated by the CrewAI engine.

The core feature is the creation and integration of a **Custom Tool** (like the `CustomerSupportDataFetcher`), which simulates fetching proprietary company data (e.g., ticket logs, resolution times). This showcases how to integrate proprietary APIs or internal data systems into an agentic workflow.

The three specialized agents and their roles are:
1.  **Data Analyst Agent:** Retrieves simulated customer data using the custom tool and performs initial analysis to uncover recurring issues and pain points.
2.  **Process Optimizer Agent:** Takes the analysis output and identifies operational bottlenecks, proposing 2-3 actionable improvements to the support process.
3.  **Executive Report Writer Agent:** Gathers the analysis and optimization recommendations, transforming them into a polished, professional report with an executive summary in Markdown format.

This project emphasizes a **modular, scalable code structure**, demonstrating the optimal way to organize agents, tasks, and tools in separate files (e.g., `agents.py`, `tasks.py`, `tools.py`) for complex applications.

### Flow Diagram
<img width="809" height="618" alt="Customer Support Analysis Crew using CrewAI" src="https://github.com/user-attachments/assets/2b9604b0-fc7c-470e-9332-c0e0331f77bb" />


---

## Project 11 – Multi-Agent System on a Low-Code Platform (N8n)

### Project Description
This project shifts focus from code-heavy development to **low-code platform integration**, demonstrating how to build a powerful Multi-Agent System (MAS) using N8n. This approach allows users to orchestrate complex agent workflows visually, without writing extensive Python code.

The core of the demo is integrating the Gemini LLM and other tools within N8n's visual workflow builder. This showcases how to:
* **Sequential Orchestration:** Set up a clear, step-by-step workflow similar to the previous CrewAI demo, but managed visually via N8n nodes.
* **Tool Abstraction:** Utilize N8n nodes to serve as "tools" for the agent, handling data parsing, formatting, and external API calls.
* **Low-Code Agent Definition:** Define the roles, goals, and backstories for multiple agents within the N8n workflow parameters.

