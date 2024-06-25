# factorial calculator using while loop
number = int(input("Enter the factorial number you want to calculate: "))
factorial = 1
fnumber = number
while fnumber>0:
    factorial = factorial * fnumber
    fnumber = fnumber-1
print("FActorial of: ", number, " is" , factorial)

