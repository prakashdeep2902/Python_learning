language = {}

name = input("Enter 1st friend : ")
lang = input("Enter fav language of 1st friend :")

language.update({name: lang})

name = input("Enter 2st friend : ")
lang = input("Enter fav language of 2st friend :")

language.update({name: lang})
name = input("Enter 2st friend : ")
lang = input("Enter fav language of 2st friend :")
language.update({name: lang})

name = input("Enter 2st friend : ")
lang = input("Enter fav language of 2st friend :")
language.update({name: lang})


print("fav lang of all friends= ", language)
