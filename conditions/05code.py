distance = int(input("Enter DIstance: "))

if distance <= 3:
    trans = "walk"
elif distance <= 15:
    trans = "bike"
else:
    trans = "CAR"

print("AI recomended you to go with ", trans)


