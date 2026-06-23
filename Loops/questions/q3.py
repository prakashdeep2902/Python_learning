num = int(input("Enter the numbers for Prime number: "))

if num == 1 or num == 2 or num == 3:
    print(f"Prime number:")
else:
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            print("Not Prime Number")
            break
        else:
            print("prime number")
