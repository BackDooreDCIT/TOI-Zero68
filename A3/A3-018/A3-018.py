inp1 = input().split()
base = int(inp1[0])
looptime = int(inp1[1])
taken = int(inp1[1])
size = list(range(1,base))
layer = []
x = base
for i in range(base):
    xy = x*x
    layer.append(xy)
    x -= 1
beforetakenlayers = len(layer)
curstr = len(layer)-1
# print(layer)
for i in range(taken):
    layer[curstr] -= 1
    taken -= 1
    if layer[curstr] == 0:
        curstr -= 1
    if taken == 0:
        break
took = layer.count(0)
aftertakenlayers = len(layer)-took
print(aftertakenlayers)