# rag_agent.py
from crewai import Agent

def get_retriever_agent(llm, knowledge_base):
    return Agent(
        role="Retriever",
        goal="Find the most relevant information from the knowledge base.",
        llm=llm,
        backstory="You search through text chunks and bring only the most useful context.",
        tools=[knowledge_base],
        allow_delegation=False
    )

def get_responder_agent(llm):
    return Agent(
        role="Responder",
        goal="Use retrieved context to answer the user clearly and accurately.",
        llm=llm,
        backstory="You specialize in answering questions using provided context.",
        allow_delegation=False
    )
