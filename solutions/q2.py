print("Enter a value:")

val = str(input())
typeOfVal = None

res = None


# check if val has a decimal point
if "." in val:
    try:
        res = float(val)
        typeOfVal = "float"
    except ValueError:
        res = val
        typeOfVal = "str"
elif val.isdigit():
    res = int(val)
    typeOfVal = "int"
else:
    res = val
    typeOfVal = "str"

print(f"Value: {res} Type: {typeOfVal}")
