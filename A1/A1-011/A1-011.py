char = input()
output = ""
a = 0
for i in range(len(char)):
    # print(a)
    x = char.count(char[a])
    output += str(x) + char[a]
    a += x
    if a == len(char):
        break
print(output)