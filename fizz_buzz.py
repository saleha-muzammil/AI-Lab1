def is_divisible_by_3(num):
    return num % 3 == 0
def is_divisible_by_5(num):
    return num % 5 == 0

def main():
    for i in range(1,50 + 1):
        if(is_divisible_by_3(i) and is_divisible_by_5(i)):
            print("FizzBuzz")
        elif(is_divisible_by_3(i)):
            print("Fizz")
        elif(is_divisible_by_5(i)):
            print("Buzz")
        else:
            print(i)
            
if __name__ == "__main__":
    main()