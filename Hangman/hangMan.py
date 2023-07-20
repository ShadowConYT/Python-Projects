from random import choice

def runGame():
    word : str = choice(['apple','banana','carrot'])
    userName: str = input("What is your Name ? >>")

    print(f'Welcome to Hangman {userName} !')

    Guessed = ''
    tries: int = 3

    while tries > 0:
        blanks: int = 0
        print('Word : ', end='')

        for char in word:
            if char in Guessed:
                print(char, end='')
            else:
                print('_',end='')
                blanks+=1
    
        print('') #blank line

        if blanks == 0:
            print('You Guessed the word')
            break

        guess: str = input('Enter a letter : ')
        if guess in Guessed:
            print('You already guessed that letter try another letter')
            continue
        Guessed+=guess

        if guess not in word:
            tries-=1
            print(f'sorry that was wrong ({tries} tries remaining)')

            if tries == 0:
                print('You ran out of chances, Try Again')
                break

if __name__ == '__main__':
    runGame()