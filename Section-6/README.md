## Section 6

## Project 13 – RAG-based Q\&A Agent using Streamlit

### Project Description
This demonstration focuses on building a simple yet fully functional Retrieval-Augmented Generation (RAG) system integrated into a user-friendly Q\&A agent. The goal is to allow a user to chat with a custom file. The agent is built using Python, the Google Generative AI library, and **Streamlit** for a quick and intuitive web interface.

The project demonstrates:
1.  **Streamlit UI Development**: Rapidly creating a web interface with inputs for the Gemini API key, model selection, and file uploading, eliminating the need for complex HTML/CSS/JavaScript.
2.  **RAG Core Functionality**: Configuring the agent to take an uploaded text file, use its content as the knowledge base, and answer specific user questions (e.g., summarization or inquiry) based *only* on that document.
3.  **Agent Logic**: Implementing session state management and conditional logic to guide the user, ensuring the agent is properly configured before allowing interaction.

### Flow Diagram
<img width="583" height="409" alt="RAG-based Q A Agent" src="https://github.com/user-attachments/assets/54cef67e-6db4-4dff-835f-e208ad957a7c" />



## Project 14 – Agentic RAG with CrewAI

### Project Description
This advanced project demonstrates the creation of an **Agentic RAG** system using the **CrewAI** framework. This architecture replaces a single LLM call with a collaborative team of specialized agents to ensure highly accurate, contextual, and verifiable retrieval and response. The agents interact with a local **Knowledge Base** (a custom file) through a dedicated **Text Tool**.

The key components and features demonstrated are:
1.  **Specialized Agent Roles**: Defining two distinct agents:
    * **Retriever Agent**: Responsible for querying the custom tool to retrieve relevant context from the knowledge base.
    * **Responder Agent**: Responsible for synthesizing a final, accurate answer based on the context provided by the Retriever Agent.
2.  **Custom Tool Integration**: Creating and configuring a custom `Text Tool` to manage and access the knowledge base data, ensuring the agents can only retrieve verifiable information from the provided source.
3.  **Collaborative Workflow**: Setting up a sequential task flow within CrewAI that mandates the Retriever Agent successfully completes its task before the Responder Agent can proceed to generate the final answer.
4.  **Verifiable Output**: Using the agentic structure to showcase detailed logs (verbose output) that trace the flow from the initial query to context retrieval and the final response synthesis.

### Flow Diagram
<img width="1134" height="587" alt="Agentic RAG with CrewAI" src="https://github.com/user-attachments/assets/d8261c26-80f4-4ca1-aefe-001970d14736" />


