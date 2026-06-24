with open("poems.txt") as FileContext:
    data = FileContext.read()
    print(data)

    # Simple and direct True/False check
    if "mard" in data:
        print("yes it's found")
    else:
        print("not found")


with open("poems.txt") as FileContext:
    data = FileContext.read()
    print(data)

    # Explicitly check that the index is not -1
    if data.find("mard") != -1:
        print("yes it's found")
    else:
        print("not found")
