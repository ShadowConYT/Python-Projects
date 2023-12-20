from random import choice
'''
    Logic: 

    Hangman is a Word Guessing Game where you will find the word by letters
    if the letter you provided is the letter presents in the actual word
    it will fill it up in the exact place where is the letter in that word 

    Example : if the word is "apple" and your input is "p" then the output look like this
    "_pp__" with this you can find what's the letter left and fill it up and win the game

    Algorithm:

    Step 1 : Take Input from the User 
    Step 2 : Create an Empty Variable
    Step 3 : then loop through the Actual word
    Step 4 : if the letter entered presents in the word then append it to the Empty Variable
    Step 5 : If not present add "_" instead of Letter.
    Step 6 : Print out all the characters using Blank space between them as shown below example
'''
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