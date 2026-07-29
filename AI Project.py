import os
from dotenv import load_dotenv
from groq import Groq

# Load .env file
load_dotenv()

# Read API key
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)

def show_banner():
    print("=" * 40)
    print("        AI Assistant")
    print("=" * 40)
show_banner()
question = input("\nAsk AI Anything: ")

try:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    print("\nAI Response:\n")
    print(response.choices[0].message.content)

except Exception as e:
    print("\nSomething went wrong!")
    print(e)
