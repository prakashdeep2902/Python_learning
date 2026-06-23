num = int(input("Enter the number for start pattern: "))

for i in range(1, num + 1):
    print("*" * i, end="")
    print("")

print("**********End of First star pattern**************")

for i in range(1, num + 1):
    print("*" * i, end="")
    print("")


print("**********End of 2nd star pattern**************")


for i in range(1, num + 1):
    print("*" * ((num - i) + 1), end="")
    print("")


print("**********End of 3rd star pattern**************")


for i in range(1, num + 1):
    if i == 1 or i == num:
        print("*" * num, end="")
        print("")
    else:
        print("*", end="")
        print(" " * (num - 2), end="")
        print("*", end="")
        print("")


n = 5
