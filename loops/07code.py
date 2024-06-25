# prime number checker

number = int(input("Enter a number"))
is_prime = True
if number > 1:
    for i in range(2, number):
        if number%i == 0:
            is_prime = False
            print(number, "is not a primne Number")
            break
        else:
            print(number, "is a prime number")






