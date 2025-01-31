def square_by_list_comprehension(list):
    return [item**2 for item in list ]

def main():
    list = [1,2,3,4,5]
    print("Squared list: ", square_by_list_comprehension(list))

if __name__ == "__main__":
    main()