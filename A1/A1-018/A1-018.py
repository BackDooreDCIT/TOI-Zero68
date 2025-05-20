roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
inp = int(input())
if inp <= 9 and inp > 0:
    print(roman[inp-1])
else:
    print("Error : Out of range")