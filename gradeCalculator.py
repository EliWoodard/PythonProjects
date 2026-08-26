import sys

print("===== Grade Calculator =====")

userGradePercent = int(input("Enter your grade: "))

if userGradePercent > 100 or userGradePercent < 0:
    print("Invalid user value")
    sys.exit()

if userGradePercent >= 90:
    userGradeLetter = 'A'
elif userGradePercent >= 80:
    userGradeLetter = 'B'
elif userGradePercent >= 70:
    userGradeLetter = 'C'
elif userGradePercent >= 60:
    userGradeLetter = 'D'
elif userGradePercent < 60 and userGradePercent >= 0 or userGradePercent > 100:
    userGradeLetter = 'F'

print(f"Your grade is {userGradeLetter}")

