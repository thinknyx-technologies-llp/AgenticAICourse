## Section 5

---

## Project 10 – Demonstration: Building a Simple Multi-Agent System using CrewAI

### Project Description
This project introduces the fundamental concepts of multi-agent orchestration using **CrewAI**, a powerful framework for defining and managing collaborative AI teams. The demonstration builds a simple yet effective two-agent system powered by **Google Gemini** and equipped with external web-searching capabilities via the **Serper Dev Tool** (also referred to as SuperDev Tool).

The system's goal is to research a topic and produce a clean, beginner-friendly markdown report.

The two agents are:
1.  **Research Agent (The Detective)**: Its role is to use the **Serper Dev Tool** to perform real-time web searches, gather insights, and compile a detailed, bullet-point search summary on the given topic.
2.  **Writer Agent (The Editor)**: Its role is to receive the raw summary from the Research Agent and transform it into a polished, clear, and well-structured explanation for beginners.

The project highlights how CrewAI acts as the **orchestrator**, connecting the agents, assigning their respective tasks, and ensuring the seamless flow of information from the researcher to the writer to achieve the final deliverable.

### Flow Diagram
<img width="852" height="468" alt="Simple Multi-Agent System " src="https://github.com/user-attachments/assets/ef1936d9-185f-4620-be41-e3726e05d438" />



## Project 11 – Customer Support Analysis Crew using CrewAI (Custom Tools & Sequential Flow)

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

## Project 12 – Multi-Agent System on a Low-Code Platform (N8n)

### Project Description
This project shifts focus from code-heavy development to **low-code platform integration**, demonstrating how to build a powerful Multi-Agent System (MAS) using N8n. This approach allows users to orchestrate complex agent workflows visually, without writing extensive Python code.

The core of the demo is integrating the Gemini LLM and other tools within N8n's visual workflow builder. This showcases how to:
* **Sequential Orchestration:** Set up a clear, step-by-step workflow similar to the previous CrewAI demo, but managed visually via N8n nodes.
* **Tool Abstraction:** Utilize N8n nodes to serve as "tools" for the agent, handling data parsing, formatting, and external API calls.
* **Low-Code Agent Definition:** Define the roles, goals, and backstories for multiple agents within the N8n workflow parameters.

---

## Project 13 – Real-World AWS Agent Using Agentic AI  

### Project Description
This project demonstrates how to build a **real-world Agentic AI system** that interacts with **AWS services** to fetch live infrastructure data, analyze it intelligently, and generate a structured cost report. The system uses **CrewAI** to orchestrate multiple agents and **Boto3** to communicate with AWS services.

The project highlights how **agentic workflows** can be applied to practical cloud monitoring and cost estimation use cases.

The key components and features demonstrated are:

1. **Specialized Agent Roles**: Defining focused agents with clear responsibilities:
   * **AWS Agent**: Acts as a senior AWS cloud engineer responsible for fetching EC2 instance data, analyzing running instances, and estimating monthly costs.
   * **Reporting Agent**: Acts as a strict data reporter that converts the analysis into a clean, structured report without adding assumptions or external interpretation.

2. **AWS Tool Integration**:  
   * A custom **EC2 Tool** built using the **Boto3 SDK** to fetch real-time EC2 instance information.
   * Secure credential handling using **environment variables** for AWS access keys and region configuration.

3. **Agentic Workflow Orchestration**:  
   * A **sequential CrewAI process** where the AWS Agent completes the analysis first.
   * The Reporting Agent then consumes the analysis output to generate the final report.

4. **Automated Report Generation**:  
   * Generates a **Markdown-based EC2 usage and cost report**.
   * Clearly lists instance count, instance IDs, usage duration, and estimated monthly pricing.

### Flow Diagram
<img width="1134" height="587" alt="AWS Agentic AI Workflow" src="https://github.com/user-attachments/assets/aws-agentic-ai-placeholder" />

---

## Project 14 – Multi-Cloud Agentic AI with CrewAI

### Project Description

This project demonstrates the creation of a **Multi-Cloud Agentic AI system** using the **CrewAI** framework. The system leverages a team of specialized AI agents to autonomously collect, analyze, and report cloud infrastructure data across **AWS** and **Google Cloud Platform (GCP)**.

Instead of relying on a single AI call, this architecture uses multiple collaborating agents to fetch real-time cloud resource information, synthesize insights, and deliver a consolidated report via email. The entire workflow is orchestrated using **CrewAI’s sequential process**, enabling implicit **Agent-to-Agent (A2A) communication**.

The key components and features demonstrated are:

1. **Specialized Agent Roles**: Defining four distinct agents with clear responsibilities:

   * **AWS Agent**: Fetches EC2 instance details and cost data from AWS.
   * **GCP Agent**: Retrieves Compute Engine instance status from Google Cloud.
   * **Analyst Agent**: Analyzes and synthesizes data from both cloud agents into a unified financial and resource report.
   * **Mailer Agent**: Sends the finalized HTML-formatted report to the reporting manager via email.

2. **Multi-Cloud Tool Integration**: Implementing custom tools to interact with AWS and GCP APIs, enabling agents to securely retrieve live cloud infrastructure and billing data.

3. **Agent-to-Agent Collaboration (A2A)**: Utilizing CrewAI’s **process and context abstraction** to enable seamless data flow between agents without manual message passing.

4. **Sequential Workflow Orchestration**: Configuring a sequential task execution model where cloud data collection, analysis, and email delivery occur in a controlled and logical order.

5. **Automated Reporting & Delivery**: Generating a clean, structured HTML report and automatically sending it to stakeholders, simulating a real-world cloud monitoring and reporting system.

### **Flow Diagram**

<img width="1134" height="587" alt="Multi-Cloud Agentic AI with CrewAI" src="https://github.com/user-attachments/assets/d8261c26-80f4-4ca1-aefe-001970d14736" />
