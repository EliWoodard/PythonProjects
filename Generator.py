def fibonacci(count):
    a = 0
    b = 1
    for _ in range(count):
        yield a
        a += b
        b = (a - b)


userInput = int(input("Enter a number to generate a sequence up to: "))

for number in fibonacci(userInput):
    print(number)