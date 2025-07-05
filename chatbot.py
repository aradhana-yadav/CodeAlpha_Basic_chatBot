def chatbot():
    print("Hi! I am your simple Chatbot.")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hello!")
        elif user_input == "how are you":
            print("Bot: I am fine, thank you.")
        elif user_input == "bye":
            print("Bot: Bye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I don't understand.")

if __name__ == "__main__":
    chatbot()
