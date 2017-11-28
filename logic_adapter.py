from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatterbot = ChatBot("Training Example",  logic_adapters=[
        "chatterbot.logic.BestMatch"])

chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train(
     "./data/viet.aiml"
)

response = chatterbot.get_response("Cháu năm nay 24 tuổi, cách đây hai tuần cháu phát hiện mình có mụn mọc lên ở dương vật, không ngứa, nhưng cháu chỉ đụng nhẹ vào thì rất dễ chảy máu. ")
print(response)

response = chatterbot.get_response("Chào bac sy")
print(response)