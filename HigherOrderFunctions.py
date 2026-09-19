students = [
    {"name": "Alice", "score": 87},
    {"name": "Bob", "score": 94},
    {"name": "Charlie", "score": 72},
    {"name": "Diana", "score": 99},
    {"name": "Evan", "score": 81}
]

userInput = input("Sort by score or name? (Enter 'score' or 'name'): ").strip().lower()

print("===== Student List =====")

if userInput == "name":
    sortedStudents = sorted(students, key=lambda student: student["name"])
else:
    sortedStudents = sorted(students, key=lambda student: student["score"], reverse=True)

for student in sortedStudents:
    print(f"{student['name']}: {student['score']}")