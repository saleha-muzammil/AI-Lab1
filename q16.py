from typing import List


def parse_list(inp: str) -> List[int]:
    return [int(num) for num in inp.split(",")]


user_input_1 = parse_list(input("Enter list of integers (separated by comma): "))


print(f"Average {sum(user_input_1) / len(user_input_1)}")