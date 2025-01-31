def count_word_frequency(words):
    frequency = {}  
    
    for word in words:
       
        word = word.lower()
        if word in frequency:
            frequency[word] += 1  
        else:
            frequency[word] = 1   
    
    return frequency


   
user_input = input("Enter a list of words separated by spaces: ")


words = user_input.split()


word_count = count_word_frequency(words)


print("\nWord Frequency Count:")
for word, count in word_count.items():
    print(f"{word}: {count}")

