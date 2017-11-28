from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatterbot = ChatBot("Training Example")
chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train(
     "./data/santa.aiml"
)

response = chatterbot.get_response("Chào ông")
print(response)

response = chatterbot.get_response("Cháu muốn xin ô tô đồ chơi, súng phun nước ạ")
print(response)



