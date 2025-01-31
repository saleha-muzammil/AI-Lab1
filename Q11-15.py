#list comprehension : squares

def square(list1):
    s=[x**2 for x in list1]
    return s


list1 = [1,2,3,4,5,6,7,8,9,10]
list1=square(list1)
print (list1)


#merging dictionaries
 
dic1 = {1: 'a', 2: 'b'}
dic2 = {1: 'c', 4: 'd'}
dic1.update(dic2)
print(dic1)

# remove duplicate from list 

def remove_duplicates(lst):
    s=set()
    return [x for x in lst if x not in s and not s.add(x)]

lst = [1,2,4,3,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
lst=remove_duplicates(lst)
print(lst)

#palindrome check 
checkpalindrome = lambda s: s == s[::-1]

s=input("Enter a string :")
print(checkpalindrome(s))

#fabonacci sequence genrator

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence
    
n = int(input("Enter the number of elements in fibonacci sequence :"))
print(fibonacci(n))

