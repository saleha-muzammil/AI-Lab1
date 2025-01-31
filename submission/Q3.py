arr=["apple","banana","orange","grape","kiwi"]
print("The original array is:",arr)

print("After adding a new element to the array")
arr.append("mango")
print(arr)

print("After removing an element from the array")
arr.remove("banana")
print(arr)


print("After converting each element to uppercase")
for i in arr:
    print(i.upper())

