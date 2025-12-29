import requests
from bs4 import BeautifulSoup

def get_ipo_data():
    url = "https://www.screener.in/ipo/recent"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find ALL tables on the page
            tables = soup.find_all('table')
            
            if tables:
                print(f"Found {len(tables)} tables on Screener.in")
                
                # Combine the HTML of all tables into one string
                # This ensures Gemini sees both 'Upcoming' and 'Recent' lists
                combined_tables = "\n".join([str(table) for table in tables])
                return combined_tables
            else:
                return "No IPO tables found."
        else:
            print(f"Failed to access Screener. Status Code: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"IPO Scraping Error: {e}")
        return None

if __name__ == "__main__":
    print("Fetching IPO Data from Screener...")
    data = get_ipo_data()
    if data:
        # Print the first 500 characters to verify we got HTML
        print("\n--- Preview of Extracted Data ---")
        print(data[:500])