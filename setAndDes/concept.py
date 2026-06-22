student = {"name": "Prakash", "age": 22, "city": "Delhi"}

print(student["age"])

print(student["name"])

print(student["city"])


user = {"name": "Alice", "age": 25, "is_admin": True}

# Using the dict() constructor
user_2 = dict(name="Bob", age=30, is_admin=False)


print(user)
print(user_2)

print(user_2["is_admin"])

user["name"] = "prakash"
user["age"] = 30

user.pop("name")
print("user is ::", user)


user_3 = dict(age=29, value=True, desc="he is good boy")
print(user_3.keys())
print(user_3.values())
print(user_3.items())

square = {x: x * x for x in range(5)}
print(square)
print(user_3.get("name"))


# set in python

# creating set

s = set(
    [
        1,
        2,
        3,
        4,
        4,
        5,
        5,
        5,
        55,
    ]
)

print("set", s)

fruits = {"apple", "banana", "cherry", "apple"}

print(fruits)

empty_ste = set()


empty_ste.update(["apple", "orange", "kiwi", "red"])
empty_ste.remove("red")
empty_ste.discard("red")
cset = empty_ste.copy()

print(empty_ste)
print(cset)


setA = {1, 2, 3, 4, 9, 17}
setB = {1, 2, 3, 4, 5, 6}

print(setA | setB)
print(setA & setB)
print(setA - setB)
print(setA ^ setB)

# # 2. Character Frequency Counter

# Take a string as input and count the frequency of each character using a dictionary.


trans = dict(aaJayo="please come", latring="toilate", phandra=15)


# word = input("enter the word you want to search: ")

# print(trans[word])


# s = set()

# word1 = input("Enter 1st word")
# s.update(word1)
# word2 = input("Enter 2st word")
# s.update(word2)
# word3 = input("Enter 3st word")
# s.update(word3)
# word4 = input("Enter 4st word")
# s.update(word4)
# word5 = input("Enter 5st word")
# s.update(word5)
# word6 = input("Enter 6st word")
# s.update(word6)
# word7 = input("Enter 7st word")
# s.update(word6)
# word8 = input("Enter 8st word")
# s.update(word8)


# print("unique set is::", s)

s1 = set([18, "18"])

s2 = set()
s2.add(20)
s2.add(20.2)
s2.add("20")

print(s1)

print(type(s2))

s3 = {"name": "prakash"}

print(type(s3))


language = {}

l1 = input("Enter First name : ")
language.update({"prakash": l1})
l2 = input("Enter 2nd name : ")
language.update({"vikash": l2})
l3 = input("Enter 3rd name : ")
language.update({"akash": l3})
l4 = input("Enter 4th name : ")
language.update({"banti": l4})


print("update one :::", language)
