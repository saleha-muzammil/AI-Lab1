def square_numbers(numbers):
    
    return [x**2 for x in numbers]


input_list = [1, 2, 3, 4, 5]
squared_list = square_numbers(input_list)
print("Original list:", input_list)
print("Squared list:", squared_list)