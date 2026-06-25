n: int = 5


print(n.bit_count())


# functions
def sum(a: int, b: int) -> int:
    return a + b


result = sum(200, 400.23)

print(result)

from typing import List, Tuple, Dict, Union

numbers: List[int] = [1, 3, 3, 5, 6, 4]

print(numbers)

# tuple
person: tuple[str, int] = ("alica", 30)


# disctinory

scores: dict[str, int] = {"alica": 90, "bob": 85}


identifier: Union[int, str] = "ID123"
