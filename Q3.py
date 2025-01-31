fruit_list = ["apple", "banana", "mango"]
for fruit in fruit_list:
    print(fruit.upper())
fruit_list.append("kiwi")
print("After adding element.")
for fruit in fruit_list:
    print(fruit.upper())
fruit_list.remove("apple")
print("After removing element.")
for fruit in fruit_list:
    print(fruit.upper())
