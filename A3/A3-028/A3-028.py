size = input().split()
placeholder = []
li = []
for i in range(int(size[0])):
    for j in range(int(size[1])):
        placeholder.append(0)
    li.append(placeholder)
    placeholder = []
loopamount = int(input())
for i in range(loopamount):
    inp = input().split()
    li[int(inp[0])][int(inp[1])] = "x"
# print(li)
for i in range(len(li)):
    for j in range(len(li[i])):
            if li[i][j] == "x":
                if j == 0:
                    x = list(li[i][j:j+1])
                    bombastic = 1
                    if i == 0:
                        if li[i][j+1] != "x":
                            li[i][j+1] += bombastic
                        if li[i+1][j] != "x":
                            li[i+1][j] += bombastic
                        if li[i+1][j+1] != "x":
                            li[i+1][j+1] += bombastic
                    elif i == len(li)-1:
                        if li[i][j+1] != "x":
                            li[i][j+1] += bombastic
                        if li[i-1][j] != "x":
                            li[i-1][j] += bombastic
                        if li[i-1][j+1] != "x":
                            li[i-1][j+1] += bombastic
                    else:
                        if li[i+1][j] != "x":
                            li[i+1][j] += bombastic
                        if li[i+1][j+1] != "x":
                            li[i+1][j+1] += bombastic
                        if li[i-1][j] != "x":
                            li[i-1][j] += bombastic
                        if li[i-1][j+1] != "x":
                            li[i-1][j+1] += bombastic
                        if li[i][j+1] != "x":
                            li[i][j+1] += bombastic
                elif j == len(li[i])-1:
                    x = list(li[i][j-1:j])
                    bombastic = 1
                    if i == 0:
                        if li[i][j-1] != "x":
                            li[i][j-1] += bombastic
                        if li[i+1][j] != "x":
                            li[i+1][j] += bombastic
                        if li[i+1][j-1] != "x":
                            li[i+1][j-1] += bombastic
                    elif i == len(li)-1:
                        if li[i][j-1] != "x":
                            li[i][j-1] += bombastic
                        if li[i-1][j] != "x":
                            li[i-1][j] += bombastic
                        if li[i-1][j-1] != "x":
                            li[i-1][j-1] += bombastic
                    else:
                        if li[i+1][j] != "x":
                            li[i+1][j] += bombastic
                        if li[i+1][j-1] != "x":
                            li[i+1][j-1] += bombastic
                        if li[i-1][j] != "x":
                            li[i-1][j] += bombastic
                        if li[i-1][j-1] != "x":
                            li[i-1][j-1] += bombastic
                        if li[i][j-1] != "x":
                            li[i][j-1] += bombastic
                else:
                    x = list(li[i][j-1:j+1])
                    bombastic = 1
                    if i == 0:
                        if li[i][j-1] != "x":
                            li[i][j-1] += bombastic
                        if li[i][j+1] != "x":
                            li[i][j+1] += bombastic
                        if li[i+1][j] != "x":
                            li[i+1][j] += bombastic
                        if li[i+1][j-1] != "x":
                            li[i+1][j-1] += bombastic
                        if li[i+1][j+1] != "x":
                            li[i+1][j+1] += bombastic
                    elif i == len(li)-1:
                        if li[i][j-1] != "x":
                            li[i][j-1] += bombastic
                        if li[i][j+1] != "x":
                            li[i][j+1] += bombastic
                        if li[i-1][j] != "x":
                            li[i-1][j] += bombastic
                        if li[i-1][j-1] != "x":
                            li[i-1][j-1] += bombastic
                        if li[i-1][j+1] != "x":
                            li[i-1][j+1] += bombastic
                    else:
                        if li[i+1][j] != "x":
                            li[i+1][j] += bombastic
                        if li[i+1][j-1] != "x":
                            li[i+1][j-1] += bombastic
                        if li[i+1][j+1] != "x":
                            li[i+1][j+1] += bombastic
                        if li[i-1][j] != "x":
                            li[i-1][j] += bombastic
                        if li[i-1][j-1] != "x":
                            li[i-1][j-1] += bombastic
                        if li[i-1][j+1] != "x":
                            li[i-1][j+1] += bombastic
                        if li[i][j-1] != "x":
                            li[i][j-1] += bombastic
                        if li[i][j+1] != "x":
                            li[i][j+1] += bombastic
# print(li)
for i in range(len(li)):
    print(*li[i], sep=' ')