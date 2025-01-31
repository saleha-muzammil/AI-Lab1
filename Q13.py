original_list = [1,5,2,3,4,2,5]
new_list = []

def remove_duplicates(original_list):
    for number in original_list:
        if number not in new_list:
            new_list.append(number)

remove_duplicates(original_list)
print(new_list)