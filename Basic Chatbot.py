import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ["hi|hello|hey", ["Hello!", "Hey there!", "Hi! How can I help you?"]],
    ["how are you?", ["I'm good, thank you! How about you?"]],
    ["what is your name?", ["I'm a chatbot!", "Call me ChatBot!"]],
    ["bye|goodbye", ["Goodbye!", "See you later!", "Bye! Have a great day!"]],
    ["(.*)", ["I'm not sure how to respond to that. Can you ask something else?"]]
]

chatbot = Chat(pairs, reflections)

print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ").lower()
    if user_input == "bye":
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
