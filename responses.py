from random import choice, randint
import json

count = 0

def get_response(user_input: str) -> str:
    global count
    
    lowered: str = user_input.lower()
    
    if lowered == "#start":
        count = 1
        return "Chat Started! Type '#stop' to stop the chat."
    
    
    while count == 1:
        if lowered == '':
            return "Well you're awfully silent..."
        elif 'hello' in lowered or 'hi' == lowered or 'hey' in lowered:
            return "Hello there!"
        elif 'how are you' in lowered or 'sup' in lowered or 'what\'s up' in lowered:
            return "Good, Thanks!"
        elif 'bye' in lowered:
            return "Cya!"
        elif 'roll a dice' in lowered:
            return f"You rolled {randint(1, 6)}"
        elif 'toss a coin' in lowered:
            return choice(["heads", "tails"])
        elif lowered == '#stop':
            count = 0
            return "Chat stopped. Type '#start' to start again."
        else:
            return choice(["Maybe try repeating that!", "I didn't catch that!", "Idk what you mean!"])
