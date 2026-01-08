# Section 3

## Project 3 – Simple Agentic AI using Smolagents

### Project Description
This demonstration introduces the Smolagents framework, an open-source Python library by Hugging Face, for building lightweight and powerful AI agents. We build a basic agent that performs a simple calculation (summing numbers from 1 to 10). The primary focus is on the fundamental structure of a Smolagent and the required setup, including the use of the `CodeAgent` and the `InferenceClientModel`. It also covers the essential step of configuring the Hugging Face authentication token `(HF_TOKEN)` for model access.


## Project 4 – Intelligent Weather Agent using Smolagents (Tool Use)

### Project Description
This project elevates the Smolagents concept by demonstrating how to equip an agent with external capabilities using Tools. We build a weather agent that receives a natural language query (e.g., "What is the temperature in Paris?") and intelligently uses the built-in `WebSearchTool` to find the current weather. This showcases the agent's ability to plan, search the web, execute the necessary code (including web scraping/data parsing logic written by the agent itself), and return a verified result. It contrasts the agentic approach with traditional multi-step, hardcoded pipelines.

### Flow Diagram
<img width="563" height="189" alt="Weather Agent using Smolagents" src="https://github.com/user-attachments/assets/b53661ea-5e83-44c8-af67-0671719094ce" />


## Project 5 – Agentic Text-to-SQL System with Self-Correction
This advanced demonstration builds an AI agent capable of translating natural language into complex SQL queries and executing them against a database. The core feature is the agent's reasoning loop and the creation of a custom `SQLEngineTool`. 

The project covers: 
1) Schema Inspection: Providing the agent with dynamic database schema information (column names, types) using SQLAlchemy. 
2) Safe Execution: Implementing the custom tool to execute the generated SQL safely. 
3) Multi-Table Joins: Demonstrating the agent's ability to handle advanced queries requiring joins and aggregations across two linked tables, showcasing its ability to reason and self-correct based on execution results.

### Flow Diagram
<img width="540" height="292" alt="Agentic Text-to-SQL" src="https://github.com/user-attachments/assets/bb1e46f7-0e13-4538-a333-7e3c5f5721f9" />


## Project 6 – Low-Code AI News Agent using N8N
This demonstration transitions from custom Python code to a visual, low-code platform using N8N (n-eight-n) for rapid AI agent development. The objective is to build a news retrieval agent that operates via a chat interface. The workflow highlights the orchestration of key components using interconnected nodes: 
1) `On Chat Trigger` as the entry point. 
2) The central `AI Agent` node. 
3) Integration with a `Chat Model` (e.g., Google Gemini). 
4) Use of `Simple Memory` for conversational context. 
5) Use of the `HTTP Request Tool` to fetch real-time news data. This project showcases how to quickly create functional, conversational agents with minimal coding.
