def FindFactorial(number:int):
    val=1  
    ans=1
    while val<=number:
        ans*=val
        val+=1

    print('Factorial is ',ans)       

number=int(input('Enter a non-negative number '))
while number<0:
    number=int(input('Enter a non-negative number '))

FindFactorial(number)
