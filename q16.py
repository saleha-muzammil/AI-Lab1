from typing import List

def AverageCalculator(list:List):
    sum=0
    for x in list:
        sum+=int(x)
    
    return sum/len(list)


list=input('Enter list ',).split(',')
print('Average is ',AverageCalculator(list))
