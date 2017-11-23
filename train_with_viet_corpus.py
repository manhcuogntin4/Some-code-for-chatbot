from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatterbot = ChatBot("Training Example")
# chatterbot.set_trainer(ChatterBotCorpusTrainer)

# chatterbot.train(
#     "./data/viet.aiml"
# )

response = chatterbot.get_response("Chào bác sĩ")
print(response)

response = chatterbot.get_response("Chào ban")
print(response)


