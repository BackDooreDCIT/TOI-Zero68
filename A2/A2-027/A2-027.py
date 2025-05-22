li = []
time = int(input())
for i in range(time):
    inp = int(input())
    li.append(inp)
li.sort()
alltop = li.count(li[len(li)-1])
print(li[len(li)-1])
print(alltop)