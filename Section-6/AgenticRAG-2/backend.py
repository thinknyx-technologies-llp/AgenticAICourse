import os
import glob
import time
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_key)


def upload_org_docs(folder_path="company_docs"):
    """
    Uploads all PDFs from the organization's folder to Gemini.
    Returns a list of Gemini File objects.
    """
    if not os.path.exists(folder_path):
        return []

    pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))
    uploaded_files = []
    
    print(f"📂 Found {len(pdf_files)} company docs. Uploading...")
    
    for path in pdf_files:
        try:
            # Upload file
            myfile = genai.upload_file(path, mime_type="application/pdf")
            uploaded_files.append(myfile)
        except Exception as e:
            print(f"❌ Error uploading {path}: {e}")
            
    # Wait for processing
    print("⏳ Processing company docs...")
    for f in uploaded_files:
        while f.state.name == "PROCESSING":
            time.sleep(2)
            f = genai.get_file(f.name)
            
    return [f for f in uploaded_files if f.state.name == "ACTIVE"]

def scrape_web_content(url):
    """
    Scrapes the text content from a given URL for the agent to read.
    """
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()    

        # Get text
        text = soup.get_text()
        
        # Break into lines and remove leading/trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # Break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # Drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text[:50000] # Limit to 50k chars to avoid token overload if site is huge
    except Exception as e:
        return f"Error scraping website: {str(e)}"

def analyze_project_feasibility(api_key, org_files, client_input, input_type="text"):
    """
    The core Agentic function.
    org_files: List of Gemini File objects (Company Knowledge)
    client_input: Either text content (from URL) or a Gemini File object (Client PDF)
    """
    genai.configure(api_key=api_key)
    
    # Define the Agent's Persona
    system_instruction = """
    You are a Senior Project Bid Manager & Technical Evaluator for our company.
    
    Your Task:
    1. Read our Company Documents (provided in context) to understand our skills, past projects, and tech stack.
    2. Analyze the Client's Project Requirement (provided as text or file).
    3. Determine if we are capable of delivering this project.
    
    Output Format:
    ## 🎯 Feasibility Decision: [YES / NO / MAYBE]
    
    ### Reasoning
    Why can or can't we do it? (Cite specific past projects or skills from our docs that match).
    
    ### Gap Analysis
    - **Matches:** What requirements do we meet perfectly?
    - **Missing:** What requirements are we missing or have no experience in?
    
    ### Tender/Govt Check
    Is this a government tender? Any specific strict compliances mentioned?
    
    ### Estimated Timeline & Budget
    (If mentioned in client doc, state it. If not, estimate based on similar past projects in our docs).
    
    ### Next Steps
    Draft a polite response or internal note on how to proceed.
    """

    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=system_instruction
    )
    
    # Prepare content for the model
    # We pass [Org File 1, Org File 2, ..., Client Input]
    content_payload = []
    content_payload.extend(org_files)
    
    if input_type == "file":
        content_payload.append(client_input) # Add client PDF
        content_payload.append("Above is the Client Project Document. Analyze it against our company docs.")
    else:
        content_payload.append(f"CLIENT PROJECT DESCRIPTION / WEBPAGE CONTENT:\n{client_input}")
    
    # Generate response
    response = model.generate_content(content_payload)
    return response.text