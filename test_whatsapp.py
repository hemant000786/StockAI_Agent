import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

sid = os.getenv("TWILIO_ACCOUNT_SID")
token = os.getenv("TWILIO_AUTH_TOKEN")

if not sid or not token:
    print("Error: Twilio credentials not found in .env")
    exit()

try:
    client = Client(sid, token)

    # The 'from_' number is Twilio's universal sandbox number
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hello from your AI Agent! 🤖',
        to='whatsapp:+919920713032'
    )

    print(f"Message sent! ID: {message.sid}")

except Exception as e:
    print(f"Error sending message: {e}")