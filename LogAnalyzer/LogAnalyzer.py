import sys

fileName = input("Add log file name(case-sensitive): ")

print("===== Log Analyzer =====")

infoCount = 0
warningCount = 0
errorCount = 0
logMessages = {}

try:
    with open(fileName, "r") as file:
        for line in file:
            if line.strip():
                if "INFO" in line:
                    infoCount += 1
                elif "WARNING" in line:
                    warningCount += 1
                elif "ERROR" in line:
                    errorCount += 1
            # Truncate message to remove date and time
            logMessage = line[20:].strip()
            # Add or increment up dictionary value of log message
            exists = logMessages.get(logMessage)
            if exists is not None:
                logMessages[logMessage] += 1
            else:
                logMessages[logMessage] = 1
    # Get the log message that occurred the most times
    highestCountedLog = max(logMessages, key=logMessages.get)
except FileNotFoundError:
    print(f"Couldn't find log {fileName}")
    sys.exit()

print(f"INFO messages: {infoCount}")
print(f"WARNING messages: {warningCount}")
print(f"ERROR messages: {errorCount}\n")
print("Most common error:")
print(highestCountedLog)
print(f"Occurrences: {logMessages[highestCountedLog]}")
