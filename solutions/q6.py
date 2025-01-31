list1 = []
list2 = []

for i in range(5):
    print("Enter a value for list1:")
    list1.append(int(input()))

for i in range(5):
    print("Enter a value for list2:")
    list2.append(int(input()))

set1 = set(list1)
set2 = set(list2)

print(f"Union: {set1.union(set2)}")
print(f"Intersection: {set1.intersection(set2)}")
print(f"Difference: {set1.difference(set2)}")

