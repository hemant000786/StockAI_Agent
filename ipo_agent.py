import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
# We import the scraping function we just created
from ipo_scrapper import get_ipo_data 

# 1. Load Environment Variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Error: GOOGLE_API_KEY not found.")
    exit()

def analyze_ipos():
    print("Step 1: Scraping Screener.in for IPO data...")
    html_data = get_ipo_data()
    
    if not html_data:
        print("Failed to fetch IPO data.")
        return None

    print("Step 2: Sending data to Gemini for filtering (Valuation > 500Cr)...")
    
    # We use the Flash model for speed and efficiency
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)

    # Prompt Engineering: We give Gemini strict instructions on what to look for
    prompt_template = ChatPromptTemplate.from_template(
        """
        You are a financial market AI assistant.
        
        I will provide you with HTML tables containing IPO data (Upcoming, Active, and Recent).
        
        Your Goal: Find significant upcoming or active IPOs.
        
        Criteria:
        1. Status: Must be "Upcoming" or currently "Active" (Open for subscription). Ignore "Listed" or closed IPOs.
        2. Valuation: Market Cap (M.Cap) must be GREATER than 500 Cr.
        
        HTML Data:
        {html_data}
        
        Response Format:
        If you find matches, draft a short, exciting WhatsApp notification message. 
        Include: Company Name, Open/Close Dates, and Market Cap.
        
        If NO matches are found, strictly reply with: "No upcoming IPOs > 500Cr found today."
        """
    )

    chain = prompt_template | llm
    
    try:
        response = chain.invoke({"html_data": html_data})
        print("\n--- IPO AGENT OUTPUT ---\n")
        print(response.content)
        return response.content
    except Exception as e:
        print(f"Error calling Gemini: {e}")
        return None

if __name__ == "__main__":
    analyze_ipos()