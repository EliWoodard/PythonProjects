class Account:
    def __init__(self, name, startingBalance, userHistory):
        self.accountName = name
        self.accountValue = startingBalance
        self.userHistory = userHistory

    def GetAccount(self):
        print(f"Account name: {self.accountName}")
        print(f"Account value: ${self.accountValue}")

    def Deposit(self, amount):
        self.accountValue += amount
        print(f"New balance is: ${self.accountValue}")
        self.userHistory.append(f"user deposited ${amount}")

    def Withdraw(self, amount):
        if amount <= self.accountValue:
            self.accountValue -= amount
            print(f"New balance is: ${self.accountValue}")
            self.userHistory.append(f"user withrawed ${amount}")
        else:
            print("Cannot withdraw more funds then available")

    def GetHistory(self):
        for instance in self.userHistory:
            print(instance)
        print(f"Total remaining balance: ${self.accountValue}")

print("===== Bank Account Manager =====")
print("1. Create Account")
print("2. View Accounts")
print("3. Deposit")
print("4. Withdraw")
print("5. View Transaction History")
print("6. Exit\n")

userInput = int(input("Choose an option: "))

accounts = {}

while(userInput != 6):
    if userInput == 1:
        username = input("New account name: ").strip()
        userStartingAmount = float(input("Starting balance: $"))
        accounts[username] = (Account(username, userStartingAmount, []))
    elif userInput == 2:
        for user in accounts:
            accounts[user].GetAccount()
    elif userInput == 3:
        selectedAccountName = input("Which account do you want to deposit into: ").strip()
        amount = float(input("How much: $"))
        accounts[selectedAccountName].Deposit(amount)
    elif userInput == 4:
        selectedAccountName = input("Which account do you want to withdraw from: ").strip()
        amount = float(input("How much: $"))
        accounts[selectedAccountName].Withdraw(amount)
    elif userInput == 5:
        selectedAccountName = input("Which account do you want to see its history: ").strip()
        accounts[selectedAccountName].GetHistory()

    userInput = int(input("Choose another option: "))