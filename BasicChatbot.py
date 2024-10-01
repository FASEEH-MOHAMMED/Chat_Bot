def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but thanks for asking!"
    elif "what is your name" in user_input:
        return "I'm a simple chatbot created to assist you."
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    elif "weather" in user_input:
        return "I can't check the weather right now, but you can look it up online!"
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M")
        return f"The current time is {current_time}."
    elif "joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "favorite color" in user_input:
        return "I don't have feelings, but I hear blue is a popular choice!"
    else:
        return "I'm sorry, I didn't understand that. Can you try rephrasing?"

def main():
    print("Welcome to the Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'bye']:
            print(chatbot_response(user_input))
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
