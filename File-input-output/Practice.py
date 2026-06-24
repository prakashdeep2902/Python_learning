# # file reading at once
# file = open("file.txt")
# print(file.read())


# print("\n")
# # read line by line

# print(file.readlines())


str = input("Enter the String....")


file1 = open("file.txt", "a")

file1.write(str)


file1.close()


# the same can be written using with statement like this

with open("file.txt") as folder:
    print(folder.read())


# you don't have to explicate
