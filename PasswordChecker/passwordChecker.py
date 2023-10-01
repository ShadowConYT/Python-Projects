def passwordChecker(password: str):
    with open('passwords.txt', 'r') as file:
        commonPasswords: list = file.read().splitlines()

    for i, common in enumerate(commonPasswords, start=1):
        if password == common:
            print(f"{password}: ❌ (#{i})")
            return
        
        if password == '':
            print("Password cannot be empty. please enter a vaild password")
            main()
            return
    
    print(f"{password}: ✅ (Unique)")
    return

def main():
    print("Welcome to the Password Checker!")
    password = input("Please enter your password: ")
    passwordChecker(password)

if __name__ == '__main__':
    main()