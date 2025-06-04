def in_bounds(y, x, height, width):
    return 0 <= y < height and 0 <= x < width

zmap = []
mapsize = input().split()
height = int(mapsize[0])
width = int(mapsize[1])

zmap = [[0 for _ in range(width)] for _ in range(height)]

pokeamount = int(input())
for _ in range(pokeamount):
    pokemon = input().split()
    pokeY = int(pokemon[0])
    pokeX = int(pokemon[1])
    if in_bounds(pokeY, pokeX, height, width):
        zmap[pokeY][pokeX] += 1

most = []
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(height):
    for j in range(width):
        if zmap[i][j] != 0:
            continue
        cur = 0
        for d in range(8):
            ny = i + dy[d]
            nx = j + dx[d]
            if in_bounds(ny, nx, height, width):
                cur += zmap[ny][nx]
        most.append(cur)

if most:
    print(max(most))
else:
    print(0)