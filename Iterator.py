userStartingNumber = int(input("Enter starting number: "))
userEndingNumber = int(input("Enter ending number: "))

while (userStartingNumber > userEndingNumber):
    print("Please ensure ending number is greater than or equal starting number.")
    userStartingNumber = int(input("Enter starting number: "))
    userEndingNumber = int(input("Enter ending number: "))

class CountUp:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        # An iterator must return itself when __iter__ is called
        return self

    def __next__(self):
        if self.current > userEndingNumber:
            raise StopIteration  # Signals the end of the loop
        
        result = self.current
        self.current += 1
        return result

counter = CountUp(userStartingNumber)
for num in counter:
    print(num)