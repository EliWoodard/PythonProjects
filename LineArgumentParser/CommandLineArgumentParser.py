import sys

if len(sys.argv) < 2:
    print("Please provide a text file that contains information to parse.")
    sys.exit()

fileName = sys.argv[1]

print("===== File Information =====")
print(f"Filename: {fileName}")

totalLines = 0
totalCharacters = 0
words = {}
currentWord = ""

with open(fileName, 'r') as file:
    for line in file:
        cleanLine = line.strip()
        for char in cleanLine:
            totalCharacters += 1
            # Check if the char is a space.
            if char == " ":
                if currentWord:
                    if currentWord not in words:
                        words[currentWord] = 1
                    else:
                        words[currentWord] += 1
                currentWord = ""
            elif char.isalpha():
                # if current char is a alphabetical character than add it to the current word that its getting
                currentWord += char
        if currentWord:
            if currentWord not in words:
                words[currentWord] = 1
            else:
                words[currentWord] += 1
        currentWord = ""

        totalLines += 1

    print(f"Number of lines: {totalLines}")
    print(f"Number of characters: {totalCharacters}")
    print(f"Number of unique words: {len(words)}")