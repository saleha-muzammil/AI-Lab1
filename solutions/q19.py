def convert_temp(temp, celsiusToFar):
    if celsiusToFar:
        return (temp * 9/5) + 32
    else:
        return (temp - 32) * 5/9
        


print("Enter a temperature:")
temp = int(input())

print("Convert to Fahrenheit? (y/n)")
celsiusToFahrenheit = input().lower() == 'y'

print("Convert to Celsius? (y/n)")
fahrenheitToCelsius = input().lower() == 'y'


if celsiusToFahrenheit:
    print(f"Final temperature: {convert_temp(temp, True)}")
elif fahrenheitToCelsius:
    print(f"Final temperature: {convert_temp(temp, False)}")

