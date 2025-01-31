int1_list = [1,2,3,4,5]
int2_list = [6,5,7,2,9]
int_set1 = set(int1_list)
int_set2 = set(int2_list)
union = int_set1.union(int_set2)
intersection = int_set1.intersection(int_set2)
difference = int_set1.difference(int_set2)
print("Union: ", union)
print("Intersection", intersection)
print("Difference: ", difference)