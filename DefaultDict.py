from collections import defaultdict

userText = input("Enter text: ")

userWords = userText.split(" ")

words = defaultdict(int)

for word in userWords:
    words[word] += 1

print(words)