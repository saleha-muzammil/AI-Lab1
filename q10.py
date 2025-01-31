def checkprime(num):

    if num > 1:
  
        for i in range(2, (num//2)+1):
      
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
def main():
    number= input("Enter Number : ")
    numb=int(number)
    checkprime(numb)
if __name__=="__main__":
    main()
