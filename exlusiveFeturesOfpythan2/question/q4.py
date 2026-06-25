from functools import reduce

tableOfSeven = [9 * i for i in range(1, 11)]


def max(a, b):
    if a > b:
        return a
    else:
        return b


reducere = reduce(max, tableOfSeven)

print(reducere)
