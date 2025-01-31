from typing import List


def Countfrequency(list:List):
    dictionary={}
    for x in list:
        val=dictionary.get(x)
        if val:
            dictionary[x]=val+1
        else:
            dictionary[x]=1

    return dictionary

list=input('List is : ').split(',')
print('Dictionary is ', Countfrequency(list))            
