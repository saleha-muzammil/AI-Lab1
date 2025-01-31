numbers = []
    
while True: # considering only integers
    numinput = input("Enter a number (or type 'done' to finish): ")
    
    if numinput.lower() == 'done':
        break
    
    if numinput.isdigit():
        numbers.append(int(numinput))
    else:
        print("Please enter a valid number")

if numbers:
    print(numbers)
    average = int(sum(numbers) / len(numbers))
    print(f"The average of the entered numbers is: {average}")
else:
    print("No numbers were entered.")