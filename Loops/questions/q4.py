num = int(input("Enter the number for factorial: "))

fact = 1
for i in range(num, 0, -1):
    fact = fact * i
print("factorial:::==>", fact)
