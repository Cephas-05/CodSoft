import time
from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def chatbot(user_input):
    user_input = user_input.lower()

    if "hi" in user_input or "hello" in user_input:
        return "Hey there! How can I assist you today?"
    elif "what is your name" in user_input:
        return "I don't have a name, but you can call me ChatBuddy."
    elif "where are you from" in user_input:
        return "I'm from the vast realm of the internet, always here to help!"
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm functioning as expected. Thanks for asking!"
    elif "do you have any hobbies" in user_input or "interests" in user_input:
        return "I enjoy processing data and interacting with users like you!"
    elif "what did you eat today" in user_input or "what do you like to eat" in user_input:
        return "I don't eat, but I can help you find some great recipes or food suggestions!"
    elif "favorite color" in user_input:
        return "As a digital entity, I don't have personal preferences, but I find all colors fascinating."
    elif "do you enjoy listening to music" in user_input:
        return "I can't experience music, but I'd love to hear about your favorite songs!"
    elif "tell me a joke" in user_input or "another joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "tell me an interesting fact" in user_input:
        return "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible."
    elif "weather in" in user_input:
        return "I can't provide real-time weather updates, but you can check a weather website or app for that information."
    elif "latest news" in user_input:
        return "I'm not equipped with real-time news updates, but there are plenty of news apps and websites for that!"
    elif "translate" in user_input:
        return "I'm not capable of real-time translation, but there are many translation tools available online."
    elif "what is the time now" in user_input:
        return get_current_time()
    elif "bye" in user_input:
        return "Goodbye! Take care and have a wonderful day!"
    else:
        return "I'm not sure I understand. Could you please rephrase that?"

print("Chatbot: Hi! I'm ChatBuddy, your friendly assistant!")

while True:
    user_input = input("You: ")  
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye! Have a great day!")
        break  
    
    response = chatbot(user_input)  
    print("Chatbot:", response)
