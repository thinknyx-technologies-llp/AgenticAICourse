## Section 4

## Project 7 – Build a Minimal MCP Server (4.3)

### Project Description
This foundational project introduces the **Model Context Protocol (MCP)** by demonstrating how to build a minimal, compliant MCP server from scratch using Python and FastAPI. The goal is to fully understand the client-server interaction governed by MCP. The server is built on a basic in-memory database and exposes two crucial JSON-RPC methods:
1.  **`discover`**: Allows clients to automatically learn about the server's available tools, returning MCP-style metadata.
2.  **`getweather`**: A simple tool that retrieves structured weather data from the in-memory database.

This project covers the full workflow: server implementation, tool definition, MCP metadata structuring, client script creation, and end-to-end testing using cURL and a dedicated Python client. It establishes the basic pattern for connecting AI agents to external capabilities.

### Flow Diagram
<img width="1067" height="605" alt="Minimal MCP Server 1" src="https://github.com/user-attachments/assets/ade7c093-ad7f-4be1-b7c5-868369149540" />


***

## Project 8 – Building an Agent on Top of an MCP Server (4.4)

### Project Description
Building upon the previous project, this demonstration creates a **fully functional Agentic AI application** that uses the established MCP server as its primary tool provider. This lightweight agent acts as the interface between the user's natural language query and the structured MCP environment.

The architecture showcases a modern agentic pattern:
1.  A user submits a query in **natural language**.
2.  An **LLM** (e.g., Google Gemini) interprets the query and extracts the necessary parameter (the city name).
3.  The agent code executes the tool call (the MCP `getweather` method) via JSON RPC.
4.  The **structured JSON data** returned by the MCP server is fed back to the **LLM** for final processing.
5.  The LLM generates a smooth, **natural language response** for the user.

This project validates the power of decoupling the agent's reasoning (LLM) from the tool's execution logic (MCP Server).

### Flow Diagram
<img width="1067" height="605" alt="Minimal MCP Server" src="https://github.com/user-attachments/assets/2872f94e-d6e8-467e-ab8f-dd8471ad8afe" />


***

## Project 9 – Demonstration: Docker MCP with Agentic AI (4.5)

### Project Description
This advanced demonstration moves beyond custom servers to showcase integration with a powerful, pre-built **Docker MCP Server** and an external AI client: **Claude Desktop** (using Sonnet 4.5).

The project focuses on the practical application of MCP for managing infrastructure:
* **Discovery and Connection**: Setting up the Docker MCP Toolkit via Docker Desktop's beta features and successfully connecting Claude Desktop as a client.
* **Tool Usage**: Using natural language queries to instruct the AI agent to perform complex Docker operations (e.g., listing, creating, and deleting containers).
* **Human-in-the-Loop (HIL)**: Demonstrating the security pattern where the AI agent requests explicit user permission before executing critical commands, providing a smooth, agentic infrastructure management experience.

This project confirms that the MCP pattern can be extended to control real-world systems like Docker, databases, and AWS, forming the basis for sophisticated IT automation agents.

### Flow Diagram
<img width="942" height="484" alt="MCP-Docker" src="https://github.com/user-attachments/assets/cb996ed0-0206-4a48-9e27-0178ee7babb1" />