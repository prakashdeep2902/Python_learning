from functools import reduce

l = [1, 2, 3, 4, 5]
squre = lambda x: x * x
sqlist = map(squre, l)
print(list(sqlist))

# filter


def even(n):
    if n % 2 == 0:
        return True
    else:
        return False


onlyEven = filter(even, l)
print(list(onlyEven))

# reducer


def sum(a, b):
    return (a * 2) * (b * 2)


print(reduce(sum, l))
