def CreateCounter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter1 = CreateCounter()
counter2 = CreateCounter()
counter3 = CreateCounter()
counter4 = CreateCounter()

print(counter1())  # Output: 1
print(counter1())  # Output: 2
print(counter2())  # Output: 1
print(counter2())  # Output: 2
print(counter3())  # Output: 1
print(counter4())  # Output: 1
print(counter1())  # Output: 3
print(counter2())  # Output: 3
print(counter3())  # Output: 2
print(counter4())  # Output: 2
print(counter1())  # Output: 4
print(counter2())  # Output: 4
print(counter3())  # Output: 3
print(counter4())  # Output: 3
