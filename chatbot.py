import openai

# Set your API key here
OPENAI_API_KEY = "your-api-key-here"

def chat_with_ai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
            messages=[{"role": "system", "content": "You are a helpful chatbot."},
                      {"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Simple AI Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = chat_with_ai(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
