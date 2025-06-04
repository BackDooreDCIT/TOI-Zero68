li = []
loopamount = int(input())
overweight = 0
overweightli = []
ogname = []
ogweigh = []
weigh = []
highestweight = ""
for i in range(loopamount):
    inp = input().split()
    rnp = inp[0]
    orp = inp[1]
    ogname.append(rnp)
    ogweigh.append(orp)
    weigh.append(int(orp))
    if int(orp) > 15:
        overweight += 1
weigh.sort(reverse=True)
for i in range(len(ogweigh)):
    if weigh[0] == int(ogweigh[i]):
        highestweight = ogname[i] + " " + ogweigh[i]
# print(li)
# print(weigh)
print(overweight)
print(highestweight)