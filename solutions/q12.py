
def remove_duplicates(lst):
    for i in lst:
        if lst.count(i) > 1:
            lst.remove(i)

    return lst

print(remove_duplicates([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))