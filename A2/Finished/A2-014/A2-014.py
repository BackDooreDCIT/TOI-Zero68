love = ["l", "o", "v", "e"]
output = ""
duplicate = 0
longestdupe = []
name1 = input().lower()
name2 = input().lower()
if len(name1) < len(name2):
    for i in range(len(name2)):
        name1 += name1[i]
        if len(name1) == len(name2):
            break
elif len(name2) < len(name1):
    for i in range(len(name1)):
        name2 += name2[i]
        if len(name2) == len(name1):
            break
for i in range(len(name1)):
    if name1[i] not in love and name2[i] not in love:
        output += "$"
    else:
        output += "w"
    if i == 0:
        pass
    else:
        if output[i] == "w" and output[i-1] == "w":
            duplicate += 1
        else:
            duplicate += 1
            longestdupe.append(duplicate)
            duplicate = 0
longestdupe.sort(reverse=True)
# if longestdupe[0] < 2:
#     output += "#"
w = output.count("w")
if w%2 != 0:
    output += str(longestdupe[0])
elif w%2 == 0:
    if longestdupe[0] < 2:
        output += "#"
print(output)