from datetime import datetime

date = datetime.strptime("2026-09-20 14:30", "%Y-%m-%d %H:%M")

nowDate = datetime.now()

if (nowDate < date):
    print("You must wait...")
elif (nowDate > date):
    print("Your time has passed...")
else:
    print("Your time is now.")