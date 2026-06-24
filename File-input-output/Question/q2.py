with open("Hi-Score.txt") as scoreData:
    name, score = scoreData.readline().strip().split("=")
    print(name, score)
    Enterscore = int(input("enter the score: "))
    if Enterscore > int(score):
        scoreData.write(f"score=${Enterscore}")
