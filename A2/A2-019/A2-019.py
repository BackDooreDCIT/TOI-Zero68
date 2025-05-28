code = input()
lower = code.lower()
licode = list(code)
lilower = list(lower)
result = ""
udupe = []
cur = 0
isb = 0
# print("licode",licode)
# print('lilower',lilower)
if "b" not in lilower:
    for j in range(len(lilower)):
        if j == 0:
            licode[j] = "B"
        elif licode[j-1] == "U" and licode[j-2] == "U" and licode[j-3] == "B":
            licode[j] = "B"
        else:
            licode[j] = "U"
        # print(licode)
        result += licode[j]
elif "u" not in lilower:
    for j in range(len(lilower)):
        if lilower[j] == 'b':
            isb += 1
        elif isb == 1:
            licode[j] = 'U'
        result += licode[j]
else:
    for j in range(len(licode)):
        # print(j)
        if licode[j] == "u" or licode[j] == "U":
            cur += 1
        else:
            udupe.append(cur)
            cur = 0
        if j == len(licode)-1:
            udupe.append(cur)
            cur = 0
    # print(udupe)
    result += "Yes " + str(max(udupe))
print(result)