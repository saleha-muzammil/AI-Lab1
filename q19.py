user_input = input("Enter input")
words = user_input.lower().split(" ")

d = dict()
for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(d)