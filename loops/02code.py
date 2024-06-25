n= int(input("Enter the limit number"))
sum =0
for i in range(1,n+1):
    if i%2==0:
        sum = sum+i
print("Sum of even numers is: ", sum) 