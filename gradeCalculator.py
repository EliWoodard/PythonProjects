import sys

print("===== Grade Calculator =====")

userGradePercent = int(input("Enter your grade: "))


if userGradePercent >= 90:
    userGradeLetter = 'A'
elif userGradePercent >= 80:
    userGradeLetter = 'B'
elif userGradePercent >= 70:
    userGradeLetter = 'C'
elif userGradePercent >= 60:
    userGradeLetter = 'D'
elif userGradePercent < 60 and userGradePercent >= 0:
    userGradeLetter = 'F'
else:
    print("Invalid user value")
    sys.exit()

print(f"Your grade is {userGradeLetter}")

