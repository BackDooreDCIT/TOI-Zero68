char = input()
pin = int(input())
if char == "H" and pin == 4567:
    print("safe unlocked")
elif char == "H":
    print("safe locked - change digit")
elif pin == 4567:
    print("safe locked - change char")
else:
    print("safe locked")