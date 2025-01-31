from enum import Enum

class Temperature(Enum):
    CELSIUS='Celsius',
    FARENHIET='Farenhiet'


def ConvertTemperature(temperature:float,type:str):
    if type==Temperature.CELSIUS:
        return (temperature-32) *5/9
    elif type==Temperature.FARENHIET:
        return temperature*9/5+32
    
print('temperature is ',ConvertTemperature(0,Temperature.FARENHIET))