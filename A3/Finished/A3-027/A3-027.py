size = input().split()
watermap = []
for i in range(int(size[0])):
    li = input().split()
    watermap.append(li)
# print(watermap)
for i in range(len(watermap)):
    if i == len(watermap)-1:
        pass
    else:
        for j in range(len(watermap[i])):
            if watermap[i][j] == "*" and watermap[i+1][j] == "-":
                watermap[i+1][j] = "1"
for i in range(len(watermap)):
    for j in range(len(watermap[i])):
        if watermap[i][j] == "1":
            watermap[i][j] = "*"
for i in range(len(watermap)):
    print(*watermap[i], sep=" ")