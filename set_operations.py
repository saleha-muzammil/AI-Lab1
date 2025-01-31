def main():
    list1 = input("Enter list 1: ").split()
    list2 = input("Enter list 2: ").split()
    print("List 1: ", list1)
    print("List 2: ", list2)

    set1  = set(list1)
    set2 = set(list2)
    
    print("Set 1: ", set1)
    print("Set 2: ", set2)

    print("Union: ", set1 | set2)
    print("Intersection: ", set1 & set2)
    print("Difference: ", set1 - set2)

if __name__ == "__main__":
    main()