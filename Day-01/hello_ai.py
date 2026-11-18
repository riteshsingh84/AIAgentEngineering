from openai import OpenAI
from dotenv import load_dotenv
import os

# Load configuration from the .env file
load_dotenv()

print("Configuration loaded successfully.")
print(f"Base URL: {os.getenv('BASE_URL')}")
print(f"API Key: {os.getenv('API_KEY')}")
print(f"Model: {os.getenv('MODEL')}")

# Create a client that communicates with Ollama
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

# Send a question to the AI model
response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[
        {
            "role": "user",
            "content": "What is Artificial Intelligence?"
        }
    ]
)

# Display the response
print(response.choices[0].message.content)
