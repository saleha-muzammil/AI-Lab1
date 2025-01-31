
# Greeting message 
name =input("Enter you name :")
age = input ("Enter your age :")

print ("Hello " + name + " you are " + age + " years old Welcome to AI Course")

#data type identification

num =int(input ("Enter a number :"))
num2= float(input ("Enter the number in float:"))
print (type(num))
print (type(num2))

#list operation 

mylist =["aun", "ali", "ahmed", "umer", "khan"]
print (mylist)
print ("my list after appending raja")
mylist.append("raja")
print (mylist)
print ("my list after removing ahmed")
mylist.remove("ahmed")
print (mylist)

print ("my list after convertin it to upper case :")
s2=[x.upper() for x in mylist]
print (s2)

#tuple unpacking 
tup = ("ahmed", "umer", "khan","ali", "shahzeb")
(a,b,*c)=tup
print (a)
print (b)

#dictionary 

d={"aun":"A", "ali":"B", "ahmed":"C", "umer":"D", "khan":"E"}
print (d)

