size = input().split()
placeholder = []
li = []
for i in range(int(size[0])):
    for j in range(int(size[1])):
        placeholder.append("0")
    li.append(placeholder)
    placeholder = []
loopamount = int(input())
for i in range(loopamount):
    inp = input().split()
    li[int(inp[0])][int(inp[1])] = "x"
# print(li)
