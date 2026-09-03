userText = input("Enter some text: ")
userText += " "

currentWord = ""
wordCounter = 0
characterCounter = 0
longestWordCounter = 0
words = {}

for character in userText:
    if character == " " and currentWord != "":
        if currentWord in words:
            words[currentWord] += 1
            wordCounter += 1
        else:
            words[currentWord] = 1
            wordCounter += 1
            longestWordCounter = max(len(currentWord), longestWordCounter)
        # reset current word
        currentWord = ""
    elif character.isalpha():
        # ignore anything but alpha characters
        characterCounter += 1
        currentWord += character.lower()

print(f"Words: {wordCounter}")
print(f"Characters: {characterCounter}")
print(f"Longest word: {longestWordCounter}")
print(f"Most common word: python: {max(words, key=words.get)}")
