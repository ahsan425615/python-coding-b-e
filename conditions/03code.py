marks = int(input("Enter your Marks: "))
if marks>100:
    print("Enter your marks between 0-100")
    exit()
if marks>=90:
    print("YOu got A grade")
elif marks>=80:
    print("You got B grade")
elif marks>=70:
    print("You got C grade")
elif marks>=60:
    print("You got D grade")
elif marks>=50:
    print("You got E grade")
else:
    print("You FAIL try next time:")