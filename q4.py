from typing import Tuple


def TupleUnpacking(tuple:Tuple):
    (first_ele,second_ele,*_)=tuple
    print('first element',first_ele)
    print('second element',second_ele)

tuple=('taha','usman','ali','tahnan','farrukh')
TupleUnpacking(tuple)