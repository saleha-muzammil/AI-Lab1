import sys

def is_valid_list_of_numbers(list):
    for i in list:
        if not i.isdigit():
            return False
    return True

def calculate_average(list):
    return sum(list) / len(list)

def main():
    list = input("Enter list of numbers: ").split()
    if not is_valid_list_of_numbers(list):
        print("Please enter a list of numbers.")
        sys.exit(1)
    list = [int(item) for item in list]
    
    print("Average:", calculate_average(list))

if __name__ == "__main__":
    main()