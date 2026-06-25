try:
    Take_input = int(input("enter the number: "))
    table = [Take_input * i for i in range(1, 11)]
    print("table: ", table)
    square_Of_Table = [Take_input**2 * i for i in range(1, 11)]
    print("ListOfsquare: ", square_Of_Table)
    even_number = [x for x in range(20) if x % 2 == 0]
    print("even Number::", even_number)

    square_Of_Table2 = [table.sort for t in table]

except Exception as e:
    print(e)
