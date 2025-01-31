def count_elements(lst):
    count_dict = {}
    for element in lst:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1
    return count_dict

elements = ['a', 'b', 'a', 'c', 'b', 'a']
element_counts = count_elements(elements)
print(element_counts)