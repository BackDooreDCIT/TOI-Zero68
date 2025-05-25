R = [0, 12, 18, 25]
T = [0, 15, 20, 30]
M = [0, 10, 15, 20]
kaimook = 0
inp1 = input().split()
inp2 = input().split()
teaBaseEnergy = ""
if inp1[0] == "H":
    kaimook = 5
elif inp1[0] == "O":
    kaimook = 3
elif inp1[0] == "J":
    kaimook = 2
if inp2[0] == "R":
    teaBaseEnergy = R[int(inp2[1])]
elif inp2[0] == "T":
    teaBaseEnergy = T[int(inp2[1])]
elif inp2[0] == "M":
    teaBaseEnergy = M[int(inp2[1])]
total = (kaimook*int(inp1[1])) + (teaBaseEnergy*int(inp2[2]))
print(total)