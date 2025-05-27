zmap = []
most = []
mapsize = input().split()
height = int(mapsize[0])
width = int(mapsize[1])
cur = 0

# for i in range(height):
#     for j in range(width):
#         li.append(0)
#     zmap.append(li)
#     li = []
# print(zmap)

zmap = [[0 for _ in range(width)] for _ in range(height)]

pokeamount = int(input())
for i in range(pokeamount):
    pokemon = input().split()
    pokeY = int(pokemon[0])
    pokeX = int(pokemon[1])
    zmap[pokeY][pokeX] += 1
# print(zmap)

for i in range(len(zmap)):
    for j in range(len(zmap[i])):
        if i == 0:
            if j == 0:
                if zmap[i][j] != 0:
                    continue
                else:
                    cur = zmap[i][j+1] + zmap[i+1][j] + zmap[i+1][j+1]
            elif j == len(zmap[i])-1:
                if zmap[i][j] != 0:
                    continue
                else:
                    cur = zmap[i][j-1] + zmap[i+1][j] + zmap[i+1][j-1]
            else:
                if zmap[i][j] != 0:
                    continue
                else:
                    cur = zmap[i][j+1] + zmap[i+1][j] + zmap[i+1][j+1] + zmap[i][j-1] + zmap[i+1][j-1]
        elif i == len(zmap)-1:
            if j == 0:
                if zmap[i][j] != 0:
                    continue
                else:
                    cur = zmap[i][j+1] + zmap[i-1][j] + zmap[i-1][j+1]
            elif j == len(zmap[i])-1:
                if zmap[i][j] != 0:
                    continue
                else:
                    cur = zmap[i][j-1] + zmap[i-1][j] + zmap[i-1][j-1]
            else:
                if zmap[i][j] != 0:
                    continue
                else:
                    cur = zmap[i][j+1] + zmap[i-1][j] + zmap[i-1][j+1] + zmap[i][j-1] + zmap[i-1][j-1]
        else:
            if j == 0:
                if zmap[i][j] != 0:
                    continue
                else:
                    cur = zmap[i][j+1] + zmap[i-1][j] + zmap[i-1][j+1] + zmap[i+1][j+1] + zmap[i+1][j]
            elif j == len(zmap[i])-1:
                if zmap[i][j] != 0:
                    continue
                else:
                    cur = zmap[i][j-1] + zmap[i-1][j] + zmap[i-1][j-1] + zmap[i+1][j-1] + zmap[i+1][j]
            else:
                if zmap[i][j] != 0:
                    continue
                else:
                    cur = zmap[i][j+1] + zmap[i-1][j] + zmap[i-1][j+1] + zmap[i][j-1] + zmap[i-1][j-1] + zmap[i+1][j+1] + zmap[i+1][j] + zmap[i+1][j-1]
        most.append(cur)

# print(zmap)
# most.sort(reverse=True)
# print(most)
# print(most[0])
if most:
    print(max(most))
else:
    print(0)