def main():
    dict1 = {"name": "Ali", "age": 25}
    dict2 = {"name": "Usman", "age": 20}
    
    print("Original dictionaries: ")
    print("Dict1: ", dict1)
    print("Dict2: ", dict2)

    dict3 = dict1 | dict2
    print("Merged dictionary: ", dict3)
    
if __name__ == "__main__":
    main()