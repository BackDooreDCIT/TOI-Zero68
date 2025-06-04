num = input().split()
li = []
for i in range(len(num)):
    if num[i] in li:
        pass
    else:
        li.append(num[i])
print(*li, sep=" ")