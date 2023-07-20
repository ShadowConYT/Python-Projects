import secrets
import string

def containsUpper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False

def containsSymbol(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False

def generatePassword(length: int, Symbols: bool, upperCase: bool ) -> str:
    combinations = string.ascii_lowercase + string.digits
    # Add uppercase letters to the combination list only when required by user input and not already present there

    if containsSymbol:
        combinations += string.punctuation
    
    if containsUpper:
        combinations += string.ascii_uppercase

    combinationsLength = len(combinations)
    new_password = ''

    for _ in range(length):
        new_password += combinations[secrets.randbelow(combinationsLength)]
    
    return new_password

if __name__ == '__main__':
    import random
    choices = random.choices([True, False])
    for i in range(0,6):
        password: str = generatePassword(10,choices,choices)
        specs: str = (f"U -> {containsUpper(password)} | S -> {containsSymbol(password)}")
        print(f"{password}, {specs}")