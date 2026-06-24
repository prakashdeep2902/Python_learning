# write a program  to generate multiplications tables from 2 to 20
#  and write it to the diffrent files place these files for a 13-year old


def createTableWithMulty(num):
    with open(f"Tables/table_of_{num}.txt", "w") as writeFile:

        for i in range(1, 11):
            sum = num * i
            writeFile.write(f"{num} x {i}={str(sum)}\n")


i = 2
while i <= 20:
    createTableWithMulty(i)
    i += 1
