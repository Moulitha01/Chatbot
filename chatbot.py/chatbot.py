def chatbot():
    print("Chatbot: Hello! I am your friendly chatbot. Type 'bye' to end the chat.")
    
    while True:
        user_input = input("You: ").lower()  # convert input to lowercase for easy comparison
        
        if user_input in ["helloo", "hi", "hey"]:
            print("Chatbot: Hi there! ")
        
        elif user_input in ["how are you", "how are you doing"]:
            print("Chatbot: I'm fine, thanks for asking! How about you?")
        
        elif user_input in ["i am fine", "i'm fine", "good", "great"]:
            print("Chatbot: That's wonderful to hear!")
        
        elif user_input in ["what is your name", "who are you"]:
            print("Chatbot: I'm a simple rule-based chatbot built in Python.")
        
        elif user_input in ["bye", "goodbye", "exit"]:
            print("Chatbot: Goodbye! Have a great day! ")
            break
        
        else:
            print("Chatbot: Sorry, I didn’t understand that. Can you rephrase?")
           
chatbot()
