year = int(input())
if year == 1500:
    print("yes")
elif year%100 == 0:
    if year%400 == 0:
        print("yes")
    else:
        print("no")
elif year%4 == 0:
    print("yes")
else:
    print("no")