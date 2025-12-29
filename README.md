# 📈 StockAI Agent

An automated financial analyst that scrapes stock market data and IPO listings, processes insights using **Google Gemini 2.5 Flash**, and sends a daily summary via **WhatsApp (Twilio)**.

## 🚀 Features
* **Automated Scraping:** Fetches data from Screener.in (or your target site).
* **AI Analysis:** Uses Gemini to filter high-potential IPOs (e.g., >500 Cr Market Cap).
* **Workflow Management:** Orchestrated with **LangGraph**.
* **Instant Alerts:** Delivers reports directly to WhatsApp.

## 🛠️ Prerequisites

Before running the agent, make sure you have the following:
* Python 3.9+ installed
* A [Google AI Studio](https://aistudio.google.com/) API Key
* A [Twilio](https://www.twilio.com/) Account (SID & Auth Token)

## ⚙️ Configuration (Important!)

To keep your API keys safe, this project uses a `.env` file. **Do not upload this file to GitHub.**

1.  **Create the file:**
    In the root directory of the project, create a new file named `.env`.

2.  **Add your secrets:**
    Copy the following format into the file and replace the placeholders with your actual keys:

    ```ini
    # Google Gemini API Key
    GOOGLE_API_KEY=your_google_api_key_here

    # Twilio Configuration
    TWILIO_ACCOUNT_SID=your_twilio_sid_here
    TWILIO_AUTH_TOKEN=your_twilio_auth_token_here
    TWILIO_FROM_NUMBER=whatsapp:+14155238886
    TWILIO_TO_NUMBER=whatsapp:+15551234567
    ```

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourName/StockAI_Agent.git](https://github.com/YourName/StockAI_Agent.git)
    cd StockAI_Agent
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## ▶️ Usage

Run the main script to trigger the agent manually:

```bash
python main.py