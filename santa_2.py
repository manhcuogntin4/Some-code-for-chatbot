from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatterbot = ChatBot("Training Example",
    logic_adapters=[
         "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter", read_only=True)

chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train(
     "./data/santa.aiml"
)

print("Type something to begin...")
while True:
    try:
     bot_input = chatterbot.get_response(None)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break

