import os
from openai import OpenAI

# Set your Gemini API key and base URL here or set them in environment variables
gemini_api_key = "AIzaSyBFbnQ9sGB9rd42AhschiCHwgxJ1jv8AvI"
gemini_base_url = "https://generativelanguage.googleapis.com/v1beta/"

client = OpenAI(
    api_key=gemini_api_key,
    base_url=gemini_base_url
)

def chat():
    print("🤖 Gemini AI Chatbot (type 'exit' to quit)\n")
    history = []

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            break

        history.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gemini-1.5-flash",
                messages=history
            )
            bot_reply = response.choices[0].message.content.strip()
            print("Bot:", bot_reply)
            history.append({"role": "assistant", "content": bot_reply})
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chat()
