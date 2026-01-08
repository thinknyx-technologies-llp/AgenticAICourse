## Section 2 

## Project 1 – Weather AI Agent from Scratch

### Project Description
This project demonstrates how to build a minimal yet powerful Weather Agent from scratch using the Google Gemini model and an external Weather API - without relying on any agent frameworks.
The agent takes a natural-language question like “What’s the weather in Paris today?”, extracts the city name using the LLM, queries a weather API, and then combines the raw data with the original question to generate a clear, human-friendly response.

It’s a practical example of how an agent’s operational layer works — connecting language understanding, reasoning, and real-world tools to produce intelligent outputs.

### Flow Diagram
<img width="1097" height="564" alt="Weather AI Agent from Scratch" src="https://github.com/user-attachments/assets/0f3bb388-32d8-44ae-b627-18b744edf47c" />


## Project 2 – Traditional AI AWS Infrastructure Agent

### Project Description

This project demonstrates a **Traditional AI-powered AWS Infrastructure Agent** built using **Flask**, **Google Gemini**, and the **AWS Boto3 SDK**. The agent processes natural language queries and directly executes AWS infrastructure actions, such as launching EC2 instances.

This architecture represents a **classic AI agent approach**, where intent understanding and execution occur in a single reactive flow, without multi-step planning or agent collaboration.

Key features demonstrated include:

1. **Intent Understanding with LLM**

   * Uses Google Gemini to interpret user requests and identify AWS actions.

2. **AWS Automation via Boto3**

   * Programmatically creates EC2 instances and related resources.

3. **Flask Web Interface**

   * Provides a simple browser-based interface for user interaction.

4. **End-to-End Execution Flow**

   * User query → AI decision → AWS resource creation → response.

### Flow Diagram

<img width="1044" height="386" alt="image" src="https://github.com/user-attachments/assets/a8cc1000-baf6-4c54-a58a-88d489a843a1" />

