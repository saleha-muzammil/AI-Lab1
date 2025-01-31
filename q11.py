from typing import List


def parse_list(inp: str) -> List[int]:
    return [int(num) for num in inp.split(",")]


user_input_1 = parse_list(input("Enter list of integers (separated by comma): "))

squared = [num * num for num in user_input_1]
for sqr in squared:
    print(sqr)