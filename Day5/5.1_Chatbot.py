"""Simple Chatbot using NLP (CO1)

Rule-based chatbot.
"""

import re

RULES = [
    (r"hi|hello|hey", "Hello! How can I help you?"),
    (r"how are you", "I'm just a bot, but I'm doing great!"),
    (r"what is your name", "I'm a simple chatbot."),
    (r"bye|goodbye", "Goodbye! Have a nice day."),
    (r"weather", "I can't check the weather, but I hope it's nice!"),
    (r"help", "You can ask me about greetings, name, or say bye."),
]


def respond(text):
    text = text.lower()
    for pattern, reply in RULES:
        if re.search(pattern, text):
            return reply
    return "I'm not sure how to respond to that. Type 'help'."


if __name__ == "__main__":
    print("Chatbot ready. Type 'quit' to exit.")
    # demo
    for u in ["hi", "what is your name", "bye"]:
        print("You:", u)
        print("Bot:", respond(u))
