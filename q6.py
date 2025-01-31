from typing import List


def parse_list(inp: str) -> List[int]:
    return [int(num) for num in inp.split(",")]


user_input_1 = set(parse_list(input("Enter list of integers (separated by comma): ")))
user_input_2 = set(parse_list(input("Enter list of integers (separated by comma): ")))

union = user_input_1.union(user_input_2)
print("Union", union)

intersection = user_input_1.intersection(user_input_2)
print("Intersection", intersection)

difference = user_input_1.difference(user_input_2)
print("Difference", difference)
