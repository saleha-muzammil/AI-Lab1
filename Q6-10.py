#set operation

lst1=[]
lst2=[]

n=int(input ("Enter the number of elements in list 1:"))

for i in range (0,n):
    ele = int(input())
    lst1.append(ele)

m=int(input ("Enter the number of elements in list 2:"))

for i in range (0,m):
    ele = int(input())
    lst2.append(ele)

set1=set(lst1)
set2=set(lst2)

print ("The union of the two sets is :")
print (set1.union(set2))

print ("The intersection of the two sets is :")
print (set1.intersection(set2))

print ("The difference of the two sets is :")   
print (set1.difference(set2))


#conditional statement 

num = int(input ("Enter the number :"))
if (num > 0 and num % 2 == 0):
    print ("The number is positive and even")
elif (num > 0 and  num % 2 != 0):
    print ("The number is positive and odd")
elif (num < 0 and num % 2 == 0):
    print ("The number is negative and even")
elif (num < 0 and num % 2 != 0):
    print ("The number is negative and odd")
elif(num == 0):
    print ("The number is zero")


#FIZZBUZZ
i=0
for i in range (1,50):
  if (i % 3 == 0 and i % 5 == 0):
    print ("FIZZBUZZ")
  elif (i % 3 == 0):
    print ("FIZZ")
  elif (i % 5 == 0):
    print ("BUZZ")
  else :
    print (i)


#function for factorial 

def factorial(n):

    for i in range (1,n):
        n=n*i
    return n

num = int(input ("Enter the number :"))
if (num < 0):
    print ("Please enter a positive number")
else:
    print ("The factorial of the number is :")
    print (factorial(num))


# prime number checker 

def isprime(n):
    if n <= 1:
        return False
    for i in range (2,n):
        if n % i == 0:
            return False
    return True

num = int(input ("Enter the number :"))
if isprime(num):
    print ("The number is prime")
else:
    print ("The number is not prime")



