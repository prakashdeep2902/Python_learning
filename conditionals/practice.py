# if elif  else ladder

age = int(input("Enter you string: "))
if age >= 18:
    print(f"You can drive a car {age}")
elif age < 0:
    print(f"you are mad {age} not valid age")

else:
    print(f"you are not allowed to drive {age}")


print("End of program")
