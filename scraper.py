import requests
from bs4 import BeautifulSoup

url = "https://www.moneycontrol.com/stocks/marketstats/nsegainer/index.php"
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all tables on the page
    tables = soup.find_all('table')
    
    print(f"I found {len(tables)} tables on the page.\n")
    
    # Loop through the first few tables and print their attributes to identify them
    for index, table in enumerate(tables[:5]): # Only looking at the first 5 to avoid clutter
        classes = table.get('class', 'No Class Found')
        print(f"Table #{index + 1} Class: {classes}")
        
        # Let's peek inside to see if it has stock data
        headers = [th.text.strip() for th in table.find_all('th')]
        if headers:
            print(f"   --> Column Headers: {headers[:4]}...") # Print first 4 columns
        print("-" * 30)

except Exception as e:
    print(f"Error: {e}")