LIST=()
LIST=(['apple','grapes','banana'])
print(LIST)
print("now removing apple")
LIST.remove("apple")
print(LIST)
print("Now Adding  tomato")
LIST.append("tomato")
print(LIST)
print("printing list in capitals letters")
LIST1=[]
for word in LIST:
    LIST1.append(word.upper())


print(LIST1)
