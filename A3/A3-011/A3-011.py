storeamount = int(input())
prices = input().split()
allpossible = []
curprice = []

for i in range(storeamount):
    curprice = prices[i:len(prices)]
    for j in range(len(curprice)):
        if j == 0:
            pass
        else:
            curprice[j] = int(curprice[j]) + int(curprice[j-1])
    for j in range(len(curprice)):
        if int(curprice[j]) not in allpossible:
            allpossible.append(int(curprice[j]))
        else:
            pass

print(len(allpossible))