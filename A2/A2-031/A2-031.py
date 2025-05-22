strlength = int(input())
line1 = input().split()
line2 = input().split()
loopamount = int(input())
mismatch = 0
for i in range(loopamount):
    changes = input().split()
    if changes[0] == "1":
        line1[int(changes[1])] = changes[2]
    elif changes[0] == "2":
        line2[int(changes[1])] = changes[2]
for i in range(strlength):
    if ((line1[i] == "A" and line2[i] == "T") or (line1[i] == "T" and line2[i] == "A")) or ((line1[i] == "C" and line2[i] == "G") or (line1[i] == "G" and line2[i] == "C")):
        mismatch += 0
    else:
        mismatch += 1
print(*line1, sep=" ")
print(*line2, sep=" ")
print(mismatch)