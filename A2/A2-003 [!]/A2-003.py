treeamount = int(input())
treesheight = input().split()
birdspos = []
for i in range(treeamount-1):
    if i == 0:
        cur = treesheight[i:i+2]
        # print(cur)
        if int(cur[0]) > int(cur[1]):
            birdpos = i
            birdspos.append(birdpos)
        else:
            birdpos = i+1
            birdspos.append(birdpos)
    else:
        cur = treesheight[i-2:i+2]
        if int(cur[1]) > int(cur[0]) and int(cur[1]) > int(cur[2]):
            birdpos = i
        
