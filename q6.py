LIST1=[]
n=3

for i in range(n):
    element=input(f"enter elemet {i+1}")
    LIST1.append(element)

print(LIST1)

#list2

LIST2=[]


for i in range(n):
    element=input(f"enter elemet {i+1}")
    LIST2.append(element)

print(LIST2)

#conversion in sets

set1=set(LIST1)
set2=set(LIST2)

print("Union :",set1 | set2) 
  
# intersection 
print("Intersection :", set1 & set2) 
  
# difference 
print("Difference :", set1- set2)

