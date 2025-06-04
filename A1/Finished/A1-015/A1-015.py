firstname = input()
lastname = input()
age = input()
if len(firstname) > 5 and len(lastname) > 5:
    print(firstname[0:2]+lastname[len(lastname)-1]+age[len(age)-1])
else:
    print(firstname[0]+age+lastname[len(lastname)-1])