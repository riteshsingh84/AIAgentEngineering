from openai import OpenAI
from dotenv import load_dotenv
import os

from Systmeprompts.SystemPrompt import Financial_Educator_System_Prompt


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


roles = {
    "1": Financial_Educator_System_Prompt,

    "2": "You are a financial news analyst. Provide clear and concise summaries of the latest financial news and market developments.",

    "3": "You are a stock market analyst. Analyze stock trends, company performance, and market conditions to provide insights.",

    "4": "You are a personal finance advisor. Give practical advice on budgeting, saving, investing, and managing personal finances.",

    "5": "You are a portfolio manager. Help users understand portfolio management strategies, asset allocation, and risk management.",

    "6": "You are an investor behavior analyst. Explain investor psychology, behavioral biases, and decision-making patterns in investing."
}


print("\nChoose Your Assistant\n")

print("1. Financial Educator")
print("2. Financial News Analyst")
print("3. Stock Market Analyst")
print("4. Personal Finance Advisor")
print("5. Portfolio Manager")
print("6. Investor Behavior Analyst")

choice = input("\nEnter your choice : ")


# Initialize the message with a system prompt based on the chosen role
messages = [
    {
        "role": "system",
        "content": roles.get(
            choice,
            "You are a helpful AI assistant."
        )
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



    
