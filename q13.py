from typing import List


def parse_list(inp: str) -> List[int]:
    return [int(num) for num in inp.split(",")]


user_input_1 = parse_list(input("Enter list of integers (separated by comma): "))

unique = []
for item in user_input_1:
    if item in unique:
        user_input_1.remove(item)
        continue
    else:
        unique.append(item)

print(user_input_1)
