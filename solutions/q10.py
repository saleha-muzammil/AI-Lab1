def square_list(lst):
    newList = []
    for i in range(len(lst)):
        newList.append(lst[i] * lst[i])
    return newList

print(square_list([1, 2, 3, 4, 5]))