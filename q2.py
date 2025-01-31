def TypeIdentification(var):
    print('type of var is ',type(var))

def ConvertToInt(var):
    var=int(var)
    TypeIdentification()

def COnvertToFloat(var):
    var = float(var)
    TypeIdentification(var)

TypeIdentification(1.2)

