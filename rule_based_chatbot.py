responses = {
    "hi": "Hello there!",
    "hello": "Hi! How can I help you today?",
    "how are you": "I'm just code, but I'm doing great!",
    "what is your name": "I'm a rule-based chatbot built for DecodeLabs.",
    "help": "You can say hi, ask my name, ask how I am, or say bye to exit.",
    "thanks": "You're welcome!",
    "what can you do": "I can chat about greetings, my name, and basic questions!",
    "who made you": "I was built by an intern during the DecodeLabs internship program.",
    "favorite color": "I'd say blue - like a classic terminal screen!",
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
}

# These end the chat loop
exit_words = ["bye", "exit", "quit"]


def get_reply(user_text):
    # .get() checks the dictionary for a match, and if there isn't one
    # it just returns the fallback message instead of crashing
    return responses.get(user_text, "I don't understand that. Type 'help' to see what I can do.")


def start_chat():
    print("Chatbot: Hello! I'm your rule-based assistant.")
    print("Chatbot: Type 'bye', 'exit', or 'quit' anytime to end the chat.\n")

    while True:
        user_input = input("You: ")

        # lowercase + strip so "Hi", "HI ", " hi" all match the same thing
        user_input = user_input.lower().strip()

        if user_input in exit_words:
            print("Chatbot: Goodbye! Have a great day!")
            break

        print("Chatbot:", get_reply(user_input))


start_chat()