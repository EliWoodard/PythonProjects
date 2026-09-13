def MilesToKilometers(miles: int) -> float:
    result = miles * 1.60934
    return result

def KilometersToMiles(kilometers: float) -> float:
    result = kilometers * 0.621371
    return result

print("===== Unit Converter =====")

miles = int(input("Enter miles: "))
print(f"{miles} miles = {MilesToKilometers(miles)} kilometers")

convertKilometers = input("Do you want to also convert kilometers(Y/N): ")

userResponse = convertKilometers.strip().lower()

if (userResponse == "y"):
    kilometers = float(input("Enter kilometers: "))
    print(f"{kilometers} kilometers = {KilometersToMiles(kilometers)} miles")
elif (userResponse == "n"):
    print("Thats ok...")
else:
    print("Unexpected value provided :(")