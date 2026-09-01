import sys
print("===== Employee Data Analyzer =====")

fileName = input("Enter filename: ")

headerData = []
structuredData = {}

try:
    with open(fileName, "r") as file:
        for line in file:
            if line.strip():
                lineValue = line.strip().split(",")
                if len(headerData) == 0:
                    for value in lineValue:
                        # Store header values in list
                        headerData.append(value)
                else:
                    for i, value in enumerate(lineValue):
                        # Store csv values in dictionary using header values as keys
                        headerKey = headerData[i]
                        if headerKey in structuredData:
                            structuredData[headerKey].append(value)
                        else:
                            structuredData[headerKey] = [value]
except FileNotFoundError:
    print(f"{fileName} was not found.")
    sys.exit()

convertedSalaries = [int(s) for s in structuredData["salary"]]

print(f"Employees: {len(structuredData["name"])}")
print(f"Average Salary: ${sum(convertedSalaries) / len(convertedSalaries)}")
print(f"Highest Salary: ${max(convertedSalaries)}")
print(f"Lowest Salary: ${min(convertedSalaries)}")

print("\nDepartments:")
# put departments into formatted list
numDepartmentInstances = {}
for value in structuredData["department"]:
    if value in numDepartmentInstances:
        numDepartmentInstances[value] += 1
    else:
        numDepartmentInstances[value] = 1

for value in numDepartmentInstances:
    print(f"{value}: {numDepartmentInstances[value]}")