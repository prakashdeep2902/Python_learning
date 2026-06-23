# write a recursive function to calculate first n natural number
def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)


num = int(input("Enter N natural number: "))
cal = sum(num)

print(f"sum of all {num} natural number is {cal}")

# write a function to remove a given word from a list and strip it at the same time


def remove(List, word):

    newList = []
    for item in List:
        newList.append(item.strip(word))

    return newList


my_list = ["prakash", "vikash", "akash", "abkash"]
new = remove(my_list, "ash")

print(new)
