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
        if j == 0:
            if li[i][j] == "x":
                pass
            else:
                x = list(li[i][j-1:j+1])
                bombastic = x.count("x")
                li[i][j] += bombastic
                if i == 0:
                    if li[i+1][j] != "x":
                        li[i+1][j] += bombastic
                    if li[i+1][j+1] != "x":
                        li[i+1][j+1] += bombastic
                elif i == len(li)-1:
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
        elif j == len(li[i])-1:
            if li[i][j] == "x":
                pass
            else:
                x = list(li[i][j-1:j+1])
                bombastic = x.count("x")
                li[i][j] += bombastic
                if i == 0:
                    if li[i+1][j] != "x":
                        li[i+1][j] += bombastic
                    if li[i+1][j-1] != "x":
                        li[i+1][j-1] += bombastic
                elif i == len(li)-1:
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
        else:
            if li[i][j] == "x":
                pass
            else:
                x = list(li[i][j-1:j+1])
                bombastic = x.count("x")
                li[i][j] += bombastic
                if i == 0:
                    if li[i+1][j] != "x":
                        li[i+1][j] += bombastic
                    if li[i+1][j-1] != "x":
                        li[i+1][j-1] += bombastic
                    if li[i+1][j+1] != "x":
                        li[i+1][j+1] += bombastic
                elif i == len(li)-1:
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
print(li)