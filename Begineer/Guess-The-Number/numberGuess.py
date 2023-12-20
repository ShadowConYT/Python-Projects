import random

#random.randint(start,end)
number: int = random.randint(1,10)
print(number)
chances = 3

while chances > 0:
    try:
        userInput: int = int(input("What is your Guess ?\n"))
    except ValueError as e:
        print('Please Enter a valid Integer')
        continue

    if userInput > number:
        chances -= 1
        print(f'Your Guess is higher than the number Try Again\n You have {chances} chances left')
    elif userInput < number:
        chances -= 1
        print(f'Your Guess is Lower than the number Try Again\n You have {chances} chances left')
    else:
        print('Hoorah! You Have Guessed the Number\n')
        break

else:
    #if loop completes without break statement then it means that all attempts are over and we have to declare
    print('You used all the tries. You Lose')