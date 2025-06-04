birth1 = []
birth2 = []
for i in range(3):
    inp = input()
    birth1.append(inp)
for i in range(3):
    inp = input()
    birth2.append(inp)
if int(birth1[0]) < int(birth2[0]):
    print("1")
elif int(birth1[0]) > int(birth2[0]):
    print("2")
else:
    if int(birth1[1]) < int(birth2[1]):
        print("1")
    elif int(birth1[1]) > int(birth2[1]):
        print("2")
    else:
        if int(birth1[2]) < int(birth2[2]):
            print("1")
        elif int(birth1[2]) > int(birth2[2]):
            print("2")
        else:
            print("0")