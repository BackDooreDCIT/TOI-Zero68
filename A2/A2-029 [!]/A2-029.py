trianglesize = int(input())
placeholder = []
triangle = []
for i in range(trianglesize):
    for j in range(i):
        placeholder.append("0")
    if len(placeholder) >= 3:
        for j in range(len(placeholder)):
            if j == 0 or j == len(placeholder)-1:
                continue
            elif i == trianglesize-1:
                placeholder[j] = "0"
            else:
                placeholder[j] = "1"
    triangle.append(placeholder)
for i in range(len(triangle)):
    print(*triangle[i], sep=" ")