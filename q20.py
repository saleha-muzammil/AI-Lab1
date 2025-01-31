def convert_temperature(value, scale):
    if scale.lower() == 'c':
       
        return (value * 9/5) + 32
    elif scale.lower() == 'f':
        
        return (value - 32) * 5/9
    else:
        raise ValueError("Invalid scale. Please use 'C' for Celsius or 'F' for Fahrenheit.")


print("Welcome to the Temperature Converter!")


temperature = float(input("Enter the temperature value: "))


scale = input("Convert to (C)elsius or (F)ahrenheit? ").strip()

try:
    if scale.lower() == 'c':
        converted = convert_temperature(temperature, 'f')
        print(f"{temperature}°F is equal to {converted:.2f}°C")
    elif scale.lower() == 'f':
        converted = convert_temperature(temperature, 'c')
        print(f"{temperature}°C is equal to {converted:.2f}°F")
    else:
        print("Invalid choice! Please enter 'C' or 'F'.")
except ValueError as e:
    print(e)


