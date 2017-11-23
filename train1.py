# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot("Ron Obvious")
conversation = [
    "Bonjour",
    "ça va!",
    "ça va et toi?",
    "Il fait beau aujourd'hui ?",
    "oui, tu vas partir en vacance ?",
    "Peut-être",
    "Au revoir"
    "Au revoir"
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)


response = chatbot.get_response("Il fait beau aujourd'hui ?")
print(response)

response = chatbot.get_response("salut cava")
print(response)

response = chatbot.get_response("bonjour")
print(response)