import os
import time
import google.generativeai as genai
import glob
from dotenv import load_dotenv

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_key)

def upload_and_process_files(pdf_paths):
    """
    Uploads PDFs to the Gemini File API and waits for processing.
    This acts as the 'Ingestion' phase of RAG.
    """
    uploaded_files = []
    print(f"📂 Uploading {len(pdf_paths)} course files...")
    
    for path in pdf_paths:
        try:
            # Upload the file
            file = genai.upload_file(path, mime_type="application/pdf")
            # print(f"   -> Uploaded '{file.display_name}' ({file.uri})")
            print(f"   -> Uploaded '{file.display_name}'")
            uploaded_files.append(file)
        except Exception as e:
            print(f"   ❌ Error uploading {path}: {e}")

    # Wait for files to be processed (Active state)
    print("⏳ Waiting for Google to process files (OCR & Indexing)...")
    for file in uploaded_files:
        while file.state.name == "PROCESSING":
            print(f"   ... Processing {file.display_name} ...")
            time.sleep(5)
            file = genai.get_file(file.name)
            
        if file.state.name != "ACTIVE":
            print(f"   ❌ Failed to process {file.display_name}")
            uploaded_files.remove(file)
    
    print("✅ All files ready!")
    return uploaded_files

# 2. Define the Agent
def create_agentic_rag(files):
    """
    Creates the Gemini Agent with the files in its context.
    """
    
    # System Instruction: Defines the 'Agent' behavior
    system_instruction = """
    You are an expert Teaching Assistant Agent. You have access to the user's course PDFs.
    
    Your Goals:
    1. Answer questions accurately based *only* on the provided files.
    2. CITATION IS MANDATORY: For every fact, you must state the Source File Name and the Page Number.
    3. If asked "Is this topic present?", scan the documents. If found, specify the Section/Chapter and Page. If not found, say so clearly.
    4. If the user asks for a specific location (e.g., "Where is the definition of X?"), provide the exact page number.
    
    Format your responses cleanly.
    """

    # We use Gemini 1.5 Flash for speed and cost, or Pro for complex reasoning
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash", 
        system_instruction=system_instruction
    )
    
    # Start a chat session with the files loaded into history
    # This is the "RAG" part—the model retrieves from this context.
    chat = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": files  # The files are passed as the initial user message/context
            }
        ]
    )
    return chat

# 3. Main Execution Loop
if __name__ == "__main__":
    # Define the folder name
    folder_path = "course-pdfs"
    
    # Check if folder exists
    if not os.path.exists(folder_path):
        print(f"❌ The folder '{folder_path}' does not exist. Please create it and add your files.")
    else:
        # Get all .pdf files from the folder]
        pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))
        
        if not pdf_files:
            print(f"❌ No PDF files found in '{folder_path}'.")
        else:
            print(f"📂 Found {len(pdf_files)} PDFs in '{folder_path}'")
            
            # Upload files using the existing function
            course_files = upload_and_process_files(pdf_files)
            
            # Initialize Agent with these files
            agent = create_agentic_rag(course_files)
            
            print("\nAgent Ready! Ask about your course materials (type 'quit' to exit).")
            print("-" * 50)
            
            while True:
                user_query = input("You: ")
                if user_query.lower() in ['quit', 'exit']:
                    break
                
                try:
                    print("Agent is thinking...")
                    response = agent.send_message(user_query)
                    print(f"Agent: {response.text}")
                    print("-" * 50)
                except Exception as e:
                    print(f"❌ Error: {e}")