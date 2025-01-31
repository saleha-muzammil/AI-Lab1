from typing import List


def RemoveDuplicates(list:List):
    new_list=[]
    for x in list:
        if x not in new_list:
            new_list.append(x)

    return new_list

list=input('List is : ').split(',')
print('new list is ',RemoveDuplicates(list))