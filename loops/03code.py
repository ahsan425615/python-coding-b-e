table_number = int(input("Enter a table number"))
for i in range(1,11):
    if i==5:
        continue
    print(table_number, 'X', i , '=', table_number*i)
    