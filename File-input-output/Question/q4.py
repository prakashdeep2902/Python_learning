with open("Donkey.txt", "r") as DonkData:
    data = DonkData.read()
    newText = data.replace("donkeys", "##########")
    with open("Donkey.txt", "w") as WriteDData:
        WriteDData.write(newText)
