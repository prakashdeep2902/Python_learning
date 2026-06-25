tableOfSeven = [9 * i for i in range(1, 11)]


def divBy5(num):
    if num % 5 == 0:
        return True
    else:
        False


fil = list(filter(divBy5, tableOfSeven))

print(fil)
