# try:
#     inp = int(input("enter any number: "))

# except Exception as e:
#     print(e)


# try:
#     p = int(input("Enter any number: "))
# except ValueError as v:
#     print(v)


# print(5 / 0)


inp1 = int(input("enter any number 1: "))
inp2 = int(input("enter any number 2: "))

if inp2 == 0:
    raise ZeroDivisionError("Hey program is not ment devide to zero")
else:
    print(f"division is: {inp1/inp2}")


# try except else


try:
    inp3 = int(input("enter any number 3: "))
    print(inp3)
except Exception as e:
    print(e)
else:
    print("Hi i in else")


# try except and finally


def main():

    try:
        inp4 = int(input("enter any number 4: "))
        print(inp4)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("hey i am in finally")


main()


# finally run after return as well
