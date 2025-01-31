

def average(int a, int b):
    return (a + b) / 2

print("Enter a number:")

done = False

while not done:
    try:
        a = int(input())
        done = True
    except ValueError:
        print("Invalid input. Please enter a number.")


done = False
while not done:
    try:
        b = int(input())
        done = True
    except ValueError:
        print("Invalid input. Please enter a number.")

print(f"Average: {average(a, b)}")

