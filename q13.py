def remove_duplicates(input_list):
    
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result



input_list = [3, 5, 2, 3, 8, 5, 10, 2]


unique_list = remove_duplicates(input_list)


print("Original list:", input_list)
print("List without duplicates:", unique_list)