num1 = int(input())
operator = input()
num2 = int(str(num1)[1] + str(num1)[0])
if operator == "+":
    total = num1+num2
    print(num1,operator,num2,"=",total)
else:
    total = num1*num2
    print(num1,operator,num2,"=",total)