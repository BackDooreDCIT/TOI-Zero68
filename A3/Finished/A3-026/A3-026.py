mapsize = input().split()
looptime = int(mapsize[0])
map1 = []
map2 = []

for i in range(looptime):
    inp = input()
    map1.append(list(inp.strip()))

# print('map1:', map1)
# print(map1)

for i in range(looptime):
    inp = input()
    map2.append(list(inp.strip()))

# print('map2:', map2)
# print('=========')

for i in range(looptime):
    for j in range(len(map1[i])):
        if map1[i][j] == "-" and map2[i][j] == "-":
            continue
        elif (map1[i][j] == "-" and map2[i][j] == "+") or (map2[i][j] == "-" and map1[i][j] == "+"):
            map1[i][j] = "+"
        elif (map1[i][j] == "-" and map2[i][j] == "x") or (map2[i][j] == "-" and map1[i][j] == "x"):
            map1[i][j] = "x"
        elif (map1[i][j] == "+" and map2[i][j] == "x") or (map2[i][j] == "+" and map1[i][j] == "x"):
            map1[i][j] = "*"

for i in range(looptime):
        print(*map1[i], sep="")