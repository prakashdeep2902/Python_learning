def avg(a, b, c):
    avg = (a + b + c) / 3
    return int(avg)


a = int(input("1: "))
b = int(input("2: "))
c = int(input("3: "))
result = avg(a, b, c)

print("average::==>", result)


#


def userAlter(user={"age": "prakash"}):
    print("user::==>", user)


user = dict()

userAlter(user)


# recursion


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


num = int(input("Enter a number: "))

a = factorial(num)

print(f"Factorial of {num} is {a}")
