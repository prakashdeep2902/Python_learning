try:
    with open("1.txt", "r") as f1, open("2.txt", "r") as f2, open("3.txt", "r") as f3:
        d1 = f1.read()
        d2 = f2.read()
        d3 = f3.read()
    print(d1)
    print(d2)
    print(d3)

except Exception as e:
    print(e)
