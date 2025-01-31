def get_numbers():
    numbers = []
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")
        
        if user_input.lower() == 'done':
            break
        
        try:
            
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    return numbers

def calculate_average(numbers):
    if not numbers:  
        return 0
    return sum(numbers) / len(numbers)


print("Welcome to the Average Calculator!")
numbers = get_numbers()

average = calculate_average(numbers)

if average != 0:
    print(f"The average of the entered numbers is: {average:.2f}")
else:
    print("No valid numbers were entered.")


