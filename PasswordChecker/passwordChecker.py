def passwordChecker(password: str):
    with open('passwords.txt', 'r') as file:
        commonPasswords: list = file.read().splitlines()
        print(commonPasswords)

def main():
    passwordChecker('password')

if __name__ == '__main__':
    main()