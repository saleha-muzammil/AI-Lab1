def average ( num1,  num2,  num3):
    return (num1+num2+num3)/3


done=False
while not done:
    try:
        num1 = int(input("Enter a number: "))
        done=True
    except ValueError:
        print("Please enter a number")

done=False

while not done:
    try:
        num2 = int(input("Enter another number: "))
        done=True
    except ValueError:
        print("Please enter a number")

done=False
while not done:
    try:
        num3 = int(input("Enter another number: "))
        done=True
    except ValueError:
        print("Please enter a number")



print("The average is",average(num1,num2,num3))


