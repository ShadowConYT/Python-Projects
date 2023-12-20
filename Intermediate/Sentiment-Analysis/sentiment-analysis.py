from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    Emoji: str
    Sentiment: str

def get_mood(text: str, *, sensitivity: str) -> Mood:
    
    polarity: float = TextBlob(text).sentiment.polarity
    friendly_threshold: float = sensitivity
    hostile_threshold: float = -sensitivity

    if polarity >= friendly_threshold:
        return Mood('😁', polarity)
    elif polarity <= hostile_threshold:
        return Mood('😔', polarity) 
    else:
        return Mood('😐', polarity)

def main():
    while True:
        text: str = input('How are you feeling? \n')
        mood: Mood = get_mood(text, sensitivity=0.5)
        print(f'You are feeling {mood.Emoji} ({mood.Sentiment})')

if __name__ == '__main__':
    main()