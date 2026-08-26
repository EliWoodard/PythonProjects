import random, string, sys

# Program header
print("===== Password Generator =====")

# Requirments from user
passwordLength = int(input("How long do you want your password to be(At least 3): "))
includeNumbers = input("Do you want to include numbers(Y/N): ").strip().lower()
includeSpecialCharacters = input("Do you want to include special characters(Y/N): ").strip().lower()

# User gaurds
if (passwordLength < 3 or (includeNumbers != 'y' and includeNumbers != 'n') or (includeSpecialCharacters != 'y' and includeSpecialCharacters != 'n')):
    print("Invalid password options")
    sys.exit()


# Define user password
userPassword = ""

# Random Generation
for i in range(1, passwordLength + 1):
    if (i % 3 == 0 and includeSpecialCharacters == "y"):
        userPassword += random.choice(string.punctuation)
    elif (i % 2 == 0 and includeNumbers == 'y'):
        userPassword += str(random.randint(0, 9))
    else:
        userPassword += random.choice(string.ascii_letters)

print(f"Generated Password: {userPassword}")