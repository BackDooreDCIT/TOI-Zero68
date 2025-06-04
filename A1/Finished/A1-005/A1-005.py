month = int(input())
day = int(input())
if month == 1 or month == 2 or (month == 3 and day < 21):
    print("winter")
elif (month == 3 and day >= 21) or month == 4 or month == 5 or (month == 6 and day < 21):
    print("spring")
elif (month == 6 and day >= 21) or month == 7 or month == 8 or (month == 9 and day < 21):
    print("summer")
else:
    print("fall")