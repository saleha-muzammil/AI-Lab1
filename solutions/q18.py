

def count_words(myList):
    dictionary = {}
    for i in myList:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary

myList = []

for i in range(5):
    print("Enter a word: ")
    myList.append(str(input()))

print(count_words(myList))