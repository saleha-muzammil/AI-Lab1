

from typing import List, Set


def GetListInput(list1:List,list2:List):
    list1=input("Enter data for list 1 split by ',' : ").split()
    list2=input("Enter data for list 2 split by ',' : ").split()

    print(list1)
    print(list2)
    
def ConvertListToSet(list:List):
    set=Set
    for ele in list:
        while list.count(ele)>1:
            list.remove(ele)
        set.add(ele)

    print('set is ',set)
    return set


list1=[]
list2=[]
GetListInput(list1,list2) 

set1=ConvertListToSet(list1)
set2=ConvertListToSet(list2) 
print('union of sets are ',set1.union(set2))
print('intersection of sets are',set1.intersection(set2))
print('difference of sets are ',set1.difference(set2)) 
