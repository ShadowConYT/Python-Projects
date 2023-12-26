from difflib import get_close_matches
import sys
import json

def load_knowledge(path: str) -> dict:
    with open(path, 'r') as f:
        return json.load(f)

def closest_match(user_question: str, questions: dict) -> str | None:
    questions = [q for q in questions]
    match = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if match:
        return match[0]

def chat_bot(knowledge: dict):
    user_input: str = input('You: ')
    if user_input.lower() == 'bye':
        return f'Bot: Bye, see you later! {sys.exit(0)}'
    
    best_match = closest_match(user_input, knowledge)

    if answer:= knowledge.get(best_match):
        return f'Bot: {answer}'
    else:
        return 'Bot: I can\'t seem to understand. try rephrasing what you just said...'

if __name__ == '__main__':
    brain: dict = load_knowledge('questions.json')
    while True:
        print(chat_bot(brain))
    