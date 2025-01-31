def PrintFibonnaci(val:int):
    first_number=0
    second_number=1
    if val>2:
        print(first_number)
        print(second_number)
    while val>2:
        print(first_number+second_number)
        temp=first_number+second_number
        first_number=second_number
        second_number=temp
        val-=1

val=int(input('Enter number '))
PrintFibonnaci(val)