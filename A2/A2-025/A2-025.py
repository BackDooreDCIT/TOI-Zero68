# infected = 3
# 60% = 2
# 20%% = 1
# safezone = 0
mapsize = input().split() # first num is xAxis, second is yAxis
xAxis = int(mapsize[0])
yAxis = int(mapsize[1])
rabbitpos = input().split() # first num is xAxis, second is yAxis
rabbitposX = int(rabbitpos[0])
rabbitposY = int(rabbitpos[1])
infectedamount = int(input())
townmap = []
for i in range(xAxis*yAxis):
    townmap.append(0)
for i in range(infectedamount):
    