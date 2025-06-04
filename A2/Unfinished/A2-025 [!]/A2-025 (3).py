mapsize = input().split()
row = int(mapsize[0])
col = int(mapsize[1])
rabbitcoords = input().split()
rabbitx = int(rabbitcoords[0])
rabbity = int(rabbitcoords[1])
bombamount = int(input())
bombcoords = []
zmap = []

for i in range(row):
    inp = list(range(0,col))
    zmap.append(inp)
# print(zmap)

for i in range(bombamount):
    inp = input().split()
    x = int(inp[0])
    y = int(inp[1])
    zmap[x][y] = "x"
# print(bombcoords)

# print(zmap)
print(zmap)
for i in range(len(zmap)):
    for j in range(len(zmap[i])):
        print("i",i)
        print("j",j)
        if zmap[i][j] == "x":
            if j == 0:
                if i == 0:
                    if zmap[i][j+1] != "x":
                        zmap[i][j+1] = "60"
                    if zmap[i-1][j] != "x":
                        zmap[i-1][j] = "60"
                    if zmap[i+1][j+1] != "x":
                        zmap[i+1][j+1] = "60"
                elif i == len(zmap[i])-1:
                    if zmap[i][j+1] != "x":
                        zmap[i][j+1] = "60"
                    if zmap[i-1][j] != "x":
                        zmap[i-1][j] = "60"
                    if zmap[i-1][j+1] != "x":
                        zmap[i-1][j+1] = "60"
                else:
                    if zmap[i][j+1] != "x":
                        zmap[i][j+1] = "60"
                    if zmap[i-1][j] != "x":
                        zmap[i-1][j] = "60"
                    if zmap[i-1][j+1] != "x":
                        zmap[i-1][j+1] = "60"
                    if zmap[i-1][j] != "x":
                        zmap[i-1][j] = "60"
                    if zmap[i+1][j+1] != "x":
                        zmap[i+1][j+1] = "60"
            elif j == len(zmap[i]):
                if i == 0:
                    if zmap[i][j-1] != "x":
                        zmap[i][j-1] = "60"
                    if zmap[i-1][j] != "x":
                        zmap[i-1][j] = "60"
                    if zmap[i+1][j-1] != "x":
                        zmap[i+1][j-1] = "60"
                elif i == len(zmap):
                    if zmap[i][j-1] != "x":
                        zmap[i][j-1] = "60"
                    if zmap[i-1][j] != "x":
                        zmap[i-1][j] = "60"
                    if zmap[i-1][j-1] != "x":
                        zmap[i-1][j-1] = "60"
                else:
                    if zmap[i][j-1] != "x":
                        zmap[i][j-1] = "60"
                    if zmap[i-1][j] != "x":
                        zmap[i-1][j] = "60"
                    if zmap[i-1][j-1] != "x":
                        zmap[i-1][j-1] = "60"
                    if zmap[i-1][j] != "x":
                        zmap[i-1][j] = "60"
                    if zmap[i+1][j-1] != "x":
                        zmap[i+1][j-1] = "60"
            else:
                if i == 0:
                    if zmap[i][j+1] != "x":
                        zmap[i][j+1] = "60"
                    if zmap[i+1][j+1] != "x":
                        zmap[i+1][j+1] = "60"
                    if zmap[i][j-1] != "x":
                        zmap[i][j-1] = "60"
                    if zmap[i+1][j-1] != "x":
                        zmap[i+1][j-1] = "60"
                    if zmap[i+1][j] != "x":
                        zmap[i+1][j] = "60"
                elif i == len(zmap[i])-1:
                    if zmap[i][j+1] != "x":
                        zmap[i][j+1] = "60"
                    if zmap[i-1][j+1] != "x":
                        zmap[i-1][j+1] = "60"
                    if zmap[i][j-1] != "x":
                        zmap[i][j-1] = "60"
                    if zmap[i-1][j-1] != "x":
                        zmap[i-1][j-1] = "60"
                    if zmap[i-1][j] != "x":
                        zmap[i-1][j] = "60"
                else:
                    if zmap[i][j+1] != "x":
                        zmap[i][j+1] = "60"
                    if zmap[i-1][j+1] != "x":
                        zmap[i-1][j+1] = "60"
                    if zmap[i][j-1] != "x":
                        zmap[i][j-1] = "60"
                    if zmap[i-1][j-1] != "x":
                        zmap[i-1][j-1] = "60"
                    if zmap[i-1][j] != "x":
                        zmap[i-1][j] = "60"
                    if zmap[i+1][j+1] != "x":
                        zmap[i+1][j+1] = "60"
                    if zmap[i+1][j-1] != "x":
                        zmap[i+1][j-1] = "60"
                    if zmap[i+1][j] != "x":
                        zmap[i+1][j] = "60"
for i in range(len(zmap)):
    for j in range(len(zmap[i])):
        if zmap[i][j] == "60":
            if j == 0:
                if i == 0:
                    if zmap[i][j+1] != "x" and zmap[i][j+1] != "60":
                        zmap[i][j+1] = "20"
                    if zmap[i-1][j] != "x" and zmap[i-1][j] != "60":
                        zmap[i-1][j] = "20"
                    if zmap[i+1][j+1] != "x" and zmap[i+1][j+1] != "60":
                        zmap[i+1][j+1] = "20"
                elif i == len(zmap[i])-1:
                    if zmap[i][j+1] != "x" and zmap[i][j+1] != "60":
                        zmap[i][j+1] = "20"
                    if zmap[i-1][j] != "x" and zmap[i-1][j] != "60":
                        zmap[i-1][j] = "20"
                    if zmap[i-1][j+1] != "x" and zmap[i-1][j+1] != "60":
                        zmap[i-1][j+1] = "20"
                else:
                    if zmap[i][j+1] != "x" and zmap[i][j+1] != "60":
                        zmap[i][j+1] = "20"
                    if zmap[i-1][j] != "x" and zmap[i-1][j] != "60":
                        zmap[i-1][j] = "20"
                    if zmap[i-1][j+1] != "x" and zmap[i-1][j+1] != "60":
                        zmap[i-1][j+1] = "20"
                    if zmap[i-1][j] != "x" and zmap[i-1][j] != "60":
                        zmap[i-1][j] = "20"
                    if zmap[i+1][j+1] != "x" and zmap[i+1][j+1] != "60":
                        zmap[i+1][j+1] = "20"
            elif j == len(zmap[i])-1:
                if i == 0:
                    if zmap[i][j-1] != "x" and zmap[i][j-1] != "60":
                        zmap[i][j-1] = "20"
                    if zmap[i-1][j] != "x" and zmap[i-1][j] != "60":
                        zmap[i-1][j] = "20"
                    if zmap[i+1][j-1] != "x" and zmap[i+1][j-1] != "60":
                        zmap[i+1][j-1] = "20"
                elif i == len(zmap[i])-1:
                    if zmap[i][j-1] != "x" and zmap[i][j-1] != "60":
                        zmap[i][j-1] = "20"
                    if zmap[i-1][j] != "x" and zmap[i-1][j] != "60":
                        zmap[i-1][j] = "20"
                    if zmap[i-1][j-1] != "x" and zmap[i-1][j-1] != "60":
                        zmap[i-1][j-1] = "20"
                else:
                    if zmap[i][j-1] != "x" and zmap[i][j-1] != "60":
                        zmap[i][j-1] = "20"
                    if zmap[i-1][j] != "x" and zmap[i-1][j] != "60":
                        zmap[i-1][j] = "20"
                    if zmap[i-1][j-1] != "x" and zmap[i-1][j-1] != "60":
                        zmap[i-1][j-1] = "20"
                    if zmap[i-1][j] != "x" and zmap[i-1][j] != "60":
                        zmap[i-1][j] = "20"
                    if zmap[i+1][j-1] != "x" and zmap[i+1][j-1] != "60":
                        zmap[i+1][j-1] = "20"
            else:
                if i == 0:
                    if zmap[i][j+1] != "x" and zmap[i][j+1] != "60":
                        zmap[i][j+1] = "20"
                    if zmap[i+1][j+1] != "x" and zmap[i+1][j+1] != "60":
                        zmap[i+1][j+1] = "20"
                    if zmap[i][j-1] != "x" and zmap[i][j-1] != "60":
                        zmap[i][j-1] = "20"
                    if zmap[i+1][j-1] != "x" and zmap[i+1][j-1] != "60":
                        zmap[i+1][j-1] = "20"
                    if zmap[i+1][j] != "x" and zmap[i+1][j] != "60":
                        zmap[i+1][j] = "20"
                elif i == len(zmap[i])-1:
                    if zmap[i][j+1] != "x" and zmap[i][j+1] != "60":
                        zmap[i][j+1] = "20"
                    if zmap[i-1][j+1] != "x" and zmap[i-1][j+1] != "60":
                        zmap[i-1][j+1] = "20"
                    if zmap[i][j-1] != "x" and zmap[i][j-1] != "60":
                        zmap[i][j-1] = "20"
                    if zmap[i-1][j-1] != "x" and zmap[i-1][j-1] != "60":
                        zmap[i-1][j-1] = "20"
                    if zmap[i-1][j] != "x" and zmap[i-1][j] != "60":
                        zmap[i-1][j] = "20"
                else:
                    if zmap[i][j+1] != "x" and zmap[i][j+1] != "60":
                        zmap[i][j+1] = "20"
                    if zmap[i-1][j+1] != "x" and zmap[i-1][j+1] != "60":
                        zmap[i-1][j+1] = "20"
                    if zmap[i][j-1] != "x" and zmap[i][j-1] != "60":
                        zmap[i][j-1] = "20"
                    if zmap[i-1][j-1] != "x" and zmap[i-1][j-1] != "60":
                        zmap[i-1][j-1] = "20"
                    if zmap[i-1][j] != "x" and zmap[i-1][j] != "60":
                        zmap[i-1][j] = "20"
                    if zmap[i+1][j+1] != "x" and zmap[i+1][j+1] != "60":
                        zmap[i+1][j+1] = "20"
                    if zmap[i+1][j-1] != "x" and zmap[i+1][j-1] != "60":
                        zmap[i+1][j-1] = "20"
                    if zmap[i+1][j] != "x" and zmap[i+1][j] != "60":
                        zmap[i+1][j] = "20"
for i in range(len(zmap)):
    for j in range(len(zmap[i])):
        if zmap[i][j] != "x" and zmap[i][j] != "60" and zmap[i][j] != "20":
            zmap[i][j] = 0
    
zero = 0
for i in range(len(zmap)):
    for j in range(len(zmap[i])):
        if zmap[i][j] == 0:
            zero += 1
rabbitchance = str(zmap[rabbitx][rabbity]) + "%"
print(zero)
print(rabbitchance)