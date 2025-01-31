def main():
    # assuming that the input in kelvin
    temperature = float(input("Enter temperature in kelvin: "))
    celsius = temperature - 273.15

    print("Calculated temperature in celsius: ", celsius)
    print("Calculated temperature in fahrenheit: ", celsius * 9/5 + 32)

if __name__ == "__main__":
    main()