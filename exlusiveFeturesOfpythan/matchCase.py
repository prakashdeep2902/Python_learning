# match-case was introduced in Python 3.10 as a form of structural pattern
# matching, similar to a switch statement but more powerful.


def check_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown Status"


print(check_status(404))
# Output: Not Found


day = "Sat"

match day:
    case "Sat" | "Sun":
        print("Weekend")
    case _:
        print("Weekday")


data = [1, 2]

match data:
    case [1, 2]:
        print("Matched exactly")
    case [1, x]:
        print(f"Second value is {x}")


person = {"name": "Alice", "age": 25}

match person:
    case {"name": name, "age": age}:
        print(f"{name} is {age} years old")


number = 15

match number:
    case x if x > 10:
        print("Greater than 10")
    case _:
        print("10 or less")
