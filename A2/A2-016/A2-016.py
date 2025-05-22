correct = input().split()
lottery = input().split()
correctnum = str(correct[1])
lotterynum = str(lottery[1])
# print(correct,lottery)
if lottery == correct:
    print("1000000")
elif lotterynum == correctnum:
    print("100000")
else:
    if lottery[0] == correct[0]:
        if lotterynum[2:4] == correctnum[2:4]:
            print("2000")
        elif lotterynum[3:4] == correctnum[3:4]:
            print("1000")
        else:
            print("20")
    else:
        if lotterynum[2:4] == correctnum[2:4]:
            print("200")
        elif lotterynum[3:4] == correctnum[3:4]:
            print("100")
        else:
            print("0")
