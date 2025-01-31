def main():
    list = ["ali", "usman", "cheema", "malik"]
    print("Original list: ", list)

    list.append("ahmed")
    print("List after appending: ", list)
    list.remove("usman")
    print("List after removing: ", list)

    upper_case_list = [name.upper() for name in list]
    print("Upper case list: ", upper_case_list)

if __name__ == "__main__":
    main()