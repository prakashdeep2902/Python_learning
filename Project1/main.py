import random


def snakeGunWaterGame():
    computerDis = {0: "snake", -1: "water", 1: "gun"}
    you_chose = input("chose snake gun and water: ")

    if you_chose == "c":
        return False

    R_num = random.randint(-1, 1)
    computerChoosen = computerDis[R_num]

    print("you Choose: ", you_chose)
    print("computer Choose: ", computerChoosen)

    if (
        computerChoosen == "snake"
        and you_chose == "water"
        or computerChoosen == "water"
        and you_chose == "gun"
        or computerChoosen == "gun"
        and you_chose == "snake"
    ):
        print("computers wins")

    elif (
        you_chose == "snake"
        and computerChoosen == "water"
        or you_chose == "water"
        and computerChoosen == "gun"
        or you_chose == "gun"
        and computerChoosen == "snake"
    ):
        print("You wins")

    else:

        print("++++++++++Game continue++++++++++")


while True:
    r = snakeGunWaterGame()
    if r == False:
        print("\U0001f4bb", end=":)")
        print("Bye Nice to play with you")
        break
