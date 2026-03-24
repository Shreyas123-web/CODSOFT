def rule_based_chatbot(user_input):
    # Convert user input to lowercase for easier pattern matching
    user_input = user_input.lower()

    # Predefined rules using if-else statements
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm doing well! How about you?"
    
    elif "your name" in user_input:
        return "I am a Rule-Based Chatbot created for the CodSoft internship."
    
    elif "task 1" in user_input:
        return "Task 1 is about building a simple chatbot with rule-based responses."
    
    elif "help" in user_input:
        return "I can answer basic questions about myself and Task 1. What do you need help with?"
    
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    
    else:
        return "I'm sorry, I don't understand that. Could you please rephrase?"

# Main loop to interact with the chatbot
print("Chatbot: Hi! Type 'bye' or 'exit' to end the conversation.")
while True:
    user_query = input("You: ")
    response = rule_based_chatbot(user_query)
    print(f"Chatbot: {response}")
    
    if response == "Goodbye! Have a great day!":
        break
