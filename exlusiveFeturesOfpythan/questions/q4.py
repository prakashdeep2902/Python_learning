try:
    Take_input = int(input("enter the number: "))
    table = [Take_input * i for i in range(1, 11)]
    with open("table.txt", "a") as tab:
        tab.write(
            f"Tabel of {Take_input} is : {str(table)} \n",
        )

except Exception as e:
    print(e)
