# create a game function


def game():
    giveScore = int(input("Enter the score: "))
    with open("Hi-Score.txt") as ReadData:
        scroe = ReadData.read()
        if scroe == "" or int(scroe) < giveScore:
            with open("Hi-Score.txt", "w") as WriteData:
                WriteData.write(str(giveScore))


game()
