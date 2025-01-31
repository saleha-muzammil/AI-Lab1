def NumberChecker(val:int):
    if val<0 :
        print(val,' is negative number')
    elif val==0:
        print(val,' is zero')
    else:
        print(val,' is positive number')

    if val%2==0:
        print(val,' is even number')
    else:
        print(val,' is odd number')

number=int(input('Enter a number : '))
NumberChecker(number)