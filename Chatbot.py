# ===============================
# Enhanced Basic Chatbot (Task 4 Extended)
# ===============================

# Predefined replies (original + more commands)
responses = {
    "hello": "Hi!",
    "hi": "Hello!",
    "how are you": "I'm fine, thanks!",
    "i am fine": "Great to hear that!",
    "what is your name": "I'm ChatBuddy, your simple bot!",
    "thank you": "You're welcome!",
    "thanks": "Anytime!",
    "bye": "Goodbye!"
}

# Chatbot function
def chatbot():
    print("Bot: Hi! I am ChatBuddy. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower().strip()
        if user_input == "bye":
            print("Bot: Goodbye!")
            break
        elif user_input in responses:
            print("Bot:", responses[user_input])
        else:
            print("Bot: Sorry, I don't understand.")

# Run the chatbot
chatbot()
