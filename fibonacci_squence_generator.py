def main():
    number = int(input("Enter a number: "))
    a, b = 0, 1
    for _ in range(number):
        print(a)
        a, b = b, a + b
        
if __name__ == "__main__":
    main()