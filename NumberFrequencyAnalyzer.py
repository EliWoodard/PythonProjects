userInput = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in userInput.split()]

dictionary = {}

for number in numbers:
    if number in dictionary:
        dictionary[number] += 1
    else:
        dictionary[number] = 1

largest = max(numbers)
smallest = min(numbers)
totalSum = sum(numbers)
length = len(numbers)

print("===== Number Analyzer =====")
print(f"Total numbers: {length} ")
print(f"Smallest: {smallest} ")
print(f"Largest: {largest} ")
print(f"Average: {totalSum / length} ")

print("Number frequency:")
for value in dictionary:
    print(f"{value}: {dictionary[value]}")