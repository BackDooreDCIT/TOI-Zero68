sizeamount = input().split()
toppings = input().split()
curprice = 0
if sizeamount[0] == "S":
    if sizeamount[1] == "R":
        curprice += 60
    else:
        curprice += 80
elif sizeamount[0] == "M":
    if sizeamount[1] == "R":
        curprice += 80
    else:
        curprice += 100
elif sizeamount[0] == "L":
    if sizeamount[1] == "R":
        curprice += 100
    else:
        curprice += 120
if toppings[0] == "N":
    curprice += 0
else:
    if toppings[0] == "P":
        curprice += (15*int(toppings[1]))
    else:
        curprice += (10*int(toppings[1]))
print(curprice)