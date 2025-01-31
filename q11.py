from typing import List


def Sqaure(list:List):
    square_list=[]
    [square_list.append(int(x)*int(x)) for x in list]
    return square_list


list=input("Enter a list ").split(',')
print('Sqaure list is ',Sqaure(list))
