def task1():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f" {name} you age {age}")


def task2():
    user_input = input("Enter a value: ")
    try:
        num = int(user_input)
        print(f" Integer ({num})")
    except ValueError:
        try:
            num = float(user_input)
            print(f" Float ({num})")
        except ValueError:
            print(f" String ({user_input})")


def task3():
    items = ["one", "two", "three"]
    items.append("four")
    items.remove("two")
    for item in items:
        print(item)


def task4():
    my_tuple = (1, 2, 3)
    first, second, _ = my_tuple
    print(f"First: {first} Second: {second}")


def task5():
    students = {"Ali": "A+", "Ahmad": "B", "Ali2": "C", "Ali3": "F", "Ali5": "D+"}
    print(students)


def task6():
    list1 = list(map(int, input("Enter list 1: ").split()))
    list2 = list(map(int, input("Enter list 2: ").split()))
    set1, set2 = set(list1), set(list2)
    print(f"Union: {set1 | set2}  , Intersection: {set1 & set2}  , Difference: {set1 - set2}")


def task7():
    num = int(input("Enter integer : "))
    print("Positive" if num > 0 else "Negative" if num < 0 else "Zero")
    print("Even" if num % 2 == 0 else "Odd")



def task8():
    for i in range(1, 51):
        print("FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i)



def task9(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Factorial: {result}")



def task10(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    for i in range(2, int(n/2) + 1):
        if n % i == 0 :
            return False
    return True



def task11(lst):
    return [x**2 for x in lst]



def task12(d1, d2):
    return {**d1, **d2}

def task13(lst):
    newlst = []
    for x in lst:
        if x not in newlst:
            newlst.append(x)
    return newlst


def task14(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


def task15(n):
    seq = [0, 1]
    for _ in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


def task16():
    numbers = []
    while True:
        num = input("Enter a number or 'done' to finish: ")
        if num.lower() == 'done':
            break
        numbers.append(float(num))
        
    if numbers:
        print(f"Average: {sum(numbers) / len(numbers)}")

def task17():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i * j:4}", end=" ")
        print()




def task18():
    users = []
    while True:
        
        username = input("Enter username : ")
        password = input("Enter  password : ")
        opt = input("login '1' or register '2' : ")
        if opt == "1":
            if {username, password} in users:
                print("Logged in")
            else:
                print("incorrect creds")
        elif opt == "2":
            registered = 0
            for regname, _ in users:
                if username == regname:
                    print("User already registered")
                    registered = 1
            if registered == 0:
                users.append({username, password}) 
                print("User registered")
            
        else:
            print("Invalid option. enter 1 or 2.")
        retry = input("Exit with '0' or Retry with any other key: ")
        if retry == "0":
            break

def task19():
    words = input("Enter words seprt by space : ").split()
    freq = {word: words.count(word) for word in set(words)}
    print(freq)


def task20():
    choice = input("Convert from 'c' or 'f'? : ").upper()
    temp = float(input("Enter temp : "))
    if choice == "C":
        print(f"{temp} C = {(temp * 9/5) + 32} F")
    elif choice == "F":
        print(f"{temp} F = {(temp - 32) * 5/9} C")

def main():
 
    print("Task 1")
    task1()
    print("Task 2")
    task2()
    print("Task 3")
    task3()
    print("Task 4")
    task4()
    print("Task 5")
    task5()
    print("Task 6")
    task6()
    print("Task 7")
    task7()
    print("Task 8")
    task8()
    print("Task 9")
    task9(5)
    print("Task 10")
    print("Prime?", task10(7))
    print("Task 11")
    print("Squares:", task11([1, 2, 3, 4]))
    print("Task 12")
    print("Merged Dict:", task12({"a": 1}, {"b": 2}))
    print("Task 13")
    print("Unique List:", task13([1, 2, 2, 3, 4, 4, 5]))
    print("Task 14")
    print("Palindrome?", task14("abcba"))
    print("Task 15")
    print("Fibonacci:", task15(10))
    print("Task 16")
    task16()
    print("Task 17")
    task17()
    print("Task 18")
    task18()
    print("Task 19")
    task19()
    print("Task 20")
    task20()

main()