list1=[]
list2=[]

print("Enter the first list")
for i in range(5):
    list1.append(input())

print ("Enter the second list")
for i in range(5):
    list2.append(input())

set1=set(list1)
set2=set(list2)

print("The first set is",set1)
print("The second set is",set2)

print("The union of the two sets is :",set1.union(set2))
print("The intersection of the two sets is",set1.intersection(set2))
print("The difference of the two sets is",set1.difference(set2))