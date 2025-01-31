def calculate_average():
    numbers = []
    while True:
        try:
            num = input("Enter a number (or 'done' to finish): ")
            if num.lower() == 'done':
                break
            numbers.append(float(num))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    if numbers:
        average = sum(numbers) / len(numbers)
        print(f"The average is: {average}")
    else:
        print("No numbers entered.")


calculate_average()