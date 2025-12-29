import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# 1. Load Environment Variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Error: GOOGLE_API_KEY not found. Please check your .env file.")
    exit()

# 2. Define the Scraper Function (The "Eyes")
def get_stock_table_html():
    url = "https://www.moneycontrol.com/stocks/marketstats/nsegainer/index.php"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            tables = soup.find_all('table')
            
            # We identified Table #2 (index 1) as the correct one
            if len(tables) > 1:
                return str(tables[1]) # Return the HTML of just that table
            else:
                return None
        else:
            return None
    except Exception as e:
        print(f"Scraping Error: {e}")
        return None

# 3. Define the Agent Logic (The "Brain")
def analyze_stocks():
    print("Step 1: Scraping MoneyControl for Top Gainers...")
    table_html = get_stock_table_html()
    
    if not table_html:
        print("Failed to retrieve stock data.")
        return

    print("Step 2: Sending data to Gemini for analysis...")
    
    # Initialize Gemini
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)

    # Create the Prompt
    # We pass the HTML directly to the LLM
    prompt_template = ChatPromptTemplate.from_template(
        """
        You are a financial analyst AI.
        
        I will provide you with HTML code representing a table of the top gaining stocks from the NSE (National Stock Exchange).
        
        Your Task:
        1. Parse the HTML to identify the top 5 stocks.
        2. Extract their Name, High Price, Low Price, and Last Price.
        3. Provide a brief, 1-sentence insight on why these sectors might be performing well (infer based on the company names).
        
        HTML Data:
        {html_data}
        
        Format your response as a clean Markdown list.
        """
    )

    # Create the Chain
    chain = prompt_template | llm
    
    # Run the Chain
    response = chain.invoke({"html_data": table_html})
    
    print("\n--- STOCK INSIGHTS REPORT ---\n")
    print(response.content)
    return response.content

if __name__ == "__main__":
    analyze_stocks()