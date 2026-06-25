import random


def GussRandamNumber(comp_num, num):

    if num > comp_num:
        print("Please Input smaller number")
        return {"status": True, "number": num}

    elif num < comp_num:
        print("Please Input bigger number")
        return {"status": True, "number": num}
    else:
        print("congratulations your is right guess")
        return {"status": False, "number": num}


comp_num = random.randint(1, 100)
count = 1
while True:
    yoursNumber = []
    num = int(input("Enter any number from 1 to 100: "))
    isBreak = GussRandamNumber(comp_num, num)
    count = +1
    if isBreak["status"] == False:
        break

print(f"you guess the correct number {count} attempts")
