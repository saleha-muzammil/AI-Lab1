integer_no = int(input("Enter integer: "))
if integer_no == 0:
    print("Integer is zero and it is even")
elif integer_no > 0:
    print("Integer is positive")
    if integer_no % 2 == 0:
        print("Integer is even")
    else:
        print("Integer is odd")
else:
    print("Integer is negative")
    if integer_no % 2 == 0:
        print("Integer is even")
    else:
        print("Integer is odd")
