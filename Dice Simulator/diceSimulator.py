import random
import time

def roll_dice(amount :int=2) -> list:
    if amount <= 0:
        raise ValueError
    
    rolls :list[int] = []
    for i in range(amount):
        random_roll :int = random.randint(1,6)
        rolls.append(random_roll)

    return rolls

def main():
    while True:
        try:
            userInput :str = input('How Many Dies You Want to Roll ? \n')

            if userInput.lower == 'exit':
                print('Thanks For Playing')
                break

            print(f"Rolling {userInput} dice... please wait....")
            #time.sleep(3)
            print(*roll_dice(int(userInput)))
        
        except ValueError:
            print("Invalid Input")

if __name__ == '__main__':
    main()
