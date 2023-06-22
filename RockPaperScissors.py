import random 
import sys

class RPS:
    def __init__(self):
        print("Welcome To the Rock Paper Scissor Inator")
        self.moves: dict={'rock':'🪨','paper':'📃','scissors':'✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())

    def play_game(self):
        userMove: str = input('What\'s your move ? \n').lower()
        AImove: str= random.choice(self.valid_moves)

        if userMove == 'exit':
            print('Thanks for Playing')
            sys.exit()

        if userMove not in self.valid_moves:
            print('Enter a Valid option')
            return self.play_game()
        
        self.displayMove(userMove,AImove)
        self.checkMove(userMove,AImove)
        
    def displayMove(self,userMove,AImove):
        print('-----')
        print(f'You used {self.moves[userMove]}') 
        # we want to return the EMOJI for that we are using moves[userMove]
        print(f'AI used {self.moves[AImove]}')
    
    def checkMove(self,userMove,AImove):
        if userMove == AImove:
            print('it\'s a Tie !')
        elif userMove == 'rock' and AImove == 'scissors':
            print('You Won')
        elif userMove == 'paper' and AImove == 'rock':
            print('You Won')
        elif userMove == 'scissors' and AImove == 'paper':
            print('You Won')
        else:
            print('AI Won')

if __name__ == '__main__':
    rps = RPS()
    while True:
        rps.play_game()