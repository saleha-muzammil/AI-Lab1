def merge_dicts(dict1, dict2):
    
    return {**dict1, **dict2}



    
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'd': 4}


merged_dict = merge_dicts(dict1, dict2)

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Merged Dictionary:", merged_dict)