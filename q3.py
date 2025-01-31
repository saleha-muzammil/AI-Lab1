from typing import List

from exceptiongroup import catch


def AddElement(list:List,name:str):
   list.append(name)
   print(name,' added')
   print('list : ',list)

def RemovElement(list:List,name:str):

    try:
        list.remove(name)
        print(name,' removed')
    except ValueError as err:
        print(name, ' not in list')
    finally:
        print('list : ',list)

def PrintInUpper(list:List[str]):
    print('list elements in upper case')
    [print(ele.upper()) for ele in list]

list=['taha','farrukh','ali','usman','tahnan']
PrintInUpper(list)