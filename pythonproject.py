#Rule Based AI Python Chatbot

import datetime
import time

name = input("Swagat h, enter your name: ")
presenthour = datetime.datetime.now().hour

if 5 <= presenthour <= 11:
   print("good morning", name)
if 11 <= presenthour <= 17:
   print("Good Afternoon, ", name)
if 17 <= presenthour <= 20:
   print("Good Evening,", name)
else:
   print("Good night, ", name)

print("Namaste! Welcome to my chatbot")
print("You can ask me basic question , type 'bye' to exit from the bot")

responses = {
    "Hello": "Hi, welcome. How can I help you?",
    "How are you": "I am very fine.Thank you",
    "who are you": "I am smart AI chatbot",
    "motivate me": "Keep going. Every bug of your project and  I am fix it with my skills",
    "Happy": "Great  to hear that",
    "functions": "learn from youtube and websites"

}


#Methods/functions to get response of chatBot
def getresponseofBot(userOuestion):
    userOuestion = userOuestion.lower()
    for eachkey in responses:
        if eachkey  in userOuestion:
            return responses[eachkey]


    return "I am not able to tell that yet. I am learning that and answer than soon it possible"
 
# #Take care input
# userInput = input("Please ask your questions:")
# reply = getresponseofBot(userInput)
# print("Bot Response :", reply)

# if "bye" in userInput.lower():
#   print("good bye")

# Chat loop
while True:

    user_input = input("You: ")

    if "bye" in user_input.lower():
        print("Bot: Goodbye!")
        break

    reply =  getresponseofBot(user_input)

    print("Bot:", reply)