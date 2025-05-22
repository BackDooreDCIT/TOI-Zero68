rgb = ["Red", "Green", "Blue"]
cmd = input().split()
output = ""
if cmd[0] == "R":
    originalstartingpos = 0
elif cmd[0] == "G":
    originalstartingpos = 1
elif cmd[0] == "B":
    originalstartingpos = 2
curpos = originalstartingpos
for i in range(int(cmd[1])):
    output += rgb[curpos]
    if curpos == 2:
        curpos = 0
    else:
        curpos += 1
    if i == int(cmd[1])-1:
        break
    else:
        output += " "
print(output)