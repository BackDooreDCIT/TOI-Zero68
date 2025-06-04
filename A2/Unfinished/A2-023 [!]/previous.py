inp = input()
txt = inp.lower()
txtli = []
a = []
ag = 0
result = ""
incorrectpos = 0
for i in range(len(txt)):
    x = txt[i]
    txtli.append(x)
# print(txtli)
if "r" not in txtli and "a" not in txtli and "b" not in txtli:
    print("unknown", len(txtli))
else:
    for i in range(len(txtli)):
        if txtli[i] == "a":
            ag += 1
        else:
            a.append(ag)
            ag = 0
        if i == 0:
            pass
        else:
            if (txtli[i] == "a" and (txtli[i-1] != "r" and txtli[i-1] != "a")) or (txtli[i] == "b" and (txtli[i-1] == "b" or txtli[i-1] == "r")):
                result = "no"
                incorrectpos = i
                break
            else:
                result = "yes"
if len(a) == 0:
    a.append(0)
a.sort(reverse=True)
if result == "yes":
    print(result,a[0])
elif result == "no":
    print(result,incorrectpos)