codelength = int(input())
code1 = str(input())
code2 = str(input())
incorrect = 0
for i in range(codelength):
    if int(code1[i]) + int(code2[i]) != 9:
        incorrect += 1
    else:
        continue
if incorrect > 0:
    print("NO", incorrect)
else:
    print("YES")
