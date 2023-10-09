import time
import string
import itertools

# Brute force attack
def bruteForce(password):
    with open("common_words.txt", "r") as file:
        word_list = file.read().splitlines()

    # Create a list of all possible combinations of letters and numbers
    for i, match in enumerate(word_list, start=1):
        if match == password:
            return f"Common Match: {match} (#{i})"
        
if __name__ == "__main__":
    start_time = time.time()
    password = input("Enter password: ")
    print(bruteForce(password))
    print(f"--- {time.time() - start_time} seconds ---")
