height = int(input())
li = []
tri = []

for i in range(height):
    curlayer = i+1
    for j in range(curlayer):
        if i == height-1:
            li.append(0)
        else:
            if j == 0 or j == i:
                li.append(0)
            else:
                li.append(1)
    tri.append(li)
    li = []

for i in range(len(tri)):
    print(*tri[i], sep=" ")