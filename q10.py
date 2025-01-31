def CheckPrime(number:int):
    val=2
    while val<=number/2:
        if(number%val==0):
            return False
        
        val+=1

    return True

if CheckPrime(5):
    print('is prime number')
else:
    print('is not prime')