from openai import OpenAI
from dotenv import load_dotenv
import os
from SystemPrompt import Financial_Assistant_System_Prompt_Educator

# Load configuration
load_dotenv()

# Create AI client
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

print("=" * 40)
print("      My AI Assistant")
print("=" * 40)

# Initialize the message with a system prompt
messages = [
    {
        "role": "system",
        "content": Financial_Assistant_System_Prompt_Educator
    }
]

# Start the conversation loop
while True:

    user_input = input("\nYou : ")

    # Save the user's message
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    if user_input.lower() == "quit":
        print("\nAI  : Goodbye! Have a great day.")
        break

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )

    ai_reply = response.choices[0].message.content

    print("\nAI :", ai_reply)

    # Save the AI's reply
    messages.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )



    
