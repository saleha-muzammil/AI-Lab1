def Remove_dups(lst):
    listt=[]
    for i in lst:
        if i not in listt:
            listt.append(i)
        else:
            continue
    return listt

lst=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
print("The list after removing duplicates is:",Remove_dups(lst))
