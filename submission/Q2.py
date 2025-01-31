inputteehee = input("Enter a number: ")

if inputteehee.isdigit():
    print("The input is an integer")
    inputteehee =  int(inputteehee)
    print("The input after changing it into integer is ",inputteehee)
elif "." in inputteehee:
    print("The input is a float")
    inputteehee = float(inputteehee)
    print("The input after changing it into float is ",inputteehee)
else:
    print("The input is a string")

