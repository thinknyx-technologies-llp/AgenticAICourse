## Section 6

## Project 15 – RAG-based Q\&A Agent using Streamlit

### Project Description
This demonstration focuses on building a simple yet fully functional Retrieval-Augmented Generation (RAG) system integrated into a user-friendly Q\&A agent. The goal is to allow a user to chat with a custom file. The agent is built using Python, the Google Generative AI library, and **Streamlit** for a quick and intuitive web interface.

The project demonstrates:
1.  **Streamlit UI Development**: Rapidly creating a web interface with inputs for the Gemini API key, model selection, and file uploading, eliminating the need for complex HTML/CSS/JavaScript.
2.  **RAG Core Functionality**: Configuring the agent to take an uploaded text file, use its content as the knowledge base, and answer specific user questions (e.g., summarization or inquiry) based *only* on that document.
3.  **Agent Logic**: Implementing session state management and conditional logic to guide the user, ensuring the agent is properly configured before allowing interaction.

### Flow Diagram
<img width="583" height="409" alt="RAG-based Q A Agent" src="https://github.com/user-attachments/assets/54cef67e-6db4-4dff-835f-e208ad957a7c" />



## Project 16 – Agentic RAG with CrewAI

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


---

## Project 17 – Agentic RAG for Course Knowledge  

### Project Description
This project demonstrates the creation of an **Agentic Retrieval-Augmented Generation (RAG)** system that enables intelligent question answering over a **custom course knowledge base**. The system uses a **Gemini LLM**, **vector embeddings**, and an **agent-based architecture** to deliver accurate, reference-backed answers.

The knowledge base consists of course PDFs, allowing the agent to respond with explanations, course names, section references, and page numbers.

The key components and features demonstrated are:

1. **Agent-Based Teaching Assistant**:  
   * A single intelligent agent acting as an expert teaching assistant.
   * The agent is guided by strict system instructions to provide clear, structured, and reference-backed responses.

2. **Knowledge Base Integration**:  
   * Course materials (PDFs) are uploaded and indexed into a **vector database**.
   * Automatic OCR, embedding generation, and indexing enable semantic search across documents.

3. **Retrieval-Augmented Generation (RAG)**:  
   * The agent retrieves relevant context from the vector database before generating responses.
   * Ensures answers are grounded in verified course content rather than hallucinated information.

4. **Explainable and Verifiable Output**:  
   * Responses include:
     * Course name
     * Section number
     * Page reference
   * Enables transparent and trustworthy learning assistance.

5. **Interactive Query Loop**:  
   * Terminal-based interface for continuous questioning.
   * Supports multiple queries in a single session with a clean exit mechanism.

### Flow Diagram
<img width="1134" height="587" alt="Agentic RAG Course Knowledge Workflow" src="https://github.com/user-attachments/assets/agentic-rag-course-placeholder" />


---

## Project 18 – Agentic Project Feasibility Checker

### Project Description

This project demonstrates a **real-world Agentic RAG system** that evaluates whether an organization can successfully execute a given project or tender. The system uses the **Gemini LLM** combined with an **organizational knowledge base** to analyze project requirements and generate a structured feasibility report.

The solution supports both **project URLs** and **document-based inputs (PDFs)** and is exposed through a simple **Streamlit frontend** for interactive analysis.

---

### **Key Components and Features**

1. **Organization Knowledge Base (RAG)**

   * Company documents are ingested into a vector database to provide contextual grounding for analysis.

2. **Project Feasibility Agent**

   * Acts as a senior bid manager and technical evaluator.
   * Determines feasibility, gaps, risks, timeline, and budget estimates.

3. **Multiple Input Methods**

   * Analyzes projects via **URLs** or **uploaded PDF documents**.

4. **Streamlit Interface**

   * Allows users to provide API keys, upload documents, and trigger feasibility analysis.
   * Displays structured results in real time.

---

### **Flow Diagram**

<img width="1134" height="587" alt="Agentic Project Feasibility Checker" src="https://github.com/user-attachments/assets/d8261c26-80f4-4ca1-aefe-001970d14736" />
