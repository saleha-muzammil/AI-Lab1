def main():
    list1 = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    print(list2)
    
            
if __name__ == "__main__":
    main()