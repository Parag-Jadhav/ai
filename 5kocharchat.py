# Define responses for different user inputs
responses = {
    "hi": "Hello! How can I help you?",
    "how are you": "I'm a chatbot, so I don't have feelings, but I'm here to assist you.",
    "bye": "Goodbye! Have a great day.",
    "default": "I'm sorry, I didn't understand that. Can you please rephrase?"
}

# Function to generate a response based on user input
def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input in responses:
        return responses[user_input]
    else:
        return responses["default"]

# Main loop to interact with the chatbot
print("Welcome to the Chatbot! You can start chatting. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print(chatbot_response(user_input))
        break
    else:
        print("Chatbot:", chatbot_response(user_input))