import time # to calculate the time required to crack the password
import string # for characters and punctuations
import itertools # for Combinations

# Brute force attack
def common_guess(password):
    with open("common_words.txt", "r") as file:
        word_list = file.read().splitlines()

    # Create a list of all possible combinations of letters and numbers
    for i, match in enumerate(word_list, start=1):
        if match == password:
            return f"Common Match: {match} (#{i})"


def brute_force(word: str, length: int, digits: bool = False, symbols: bool = False):
    chars =  string.ascii_lowercase
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation
    
    attempts = 0
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        guess: str = "".join(guess)

        if guess == word:
            return f"Password is {guess}, found in {attempts} attempts."
        print(guess)

if __name__ == "__main__":
    start_time = time.perf_counter()
    wordtocrack = input("Enter a Word: ")
    if common:= common_guess(wordtocrack):
        print(common)
    else:
        for i in range(2,7):
            if brute:= brute_force(wordtocrack, length=i):
                print(brute)
                continue

            else:
                print("No Match")
                break

    end_time = time.perf_counter()
    if brute:
        print(f"it took {round(end_time - start_time,2)}s to crack")