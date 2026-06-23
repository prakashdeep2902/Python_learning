# char containe less then 10 char

char = input("Enter the word: ")


if len(char) < 10:
    print(f"{char} Length is less then 10 that is :{len(char)}")
else:
    print(f"{char} Length is greater then 10 that is :{len(char)}")
