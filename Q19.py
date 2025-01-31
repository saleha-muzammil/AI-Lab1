def count_word_frequency(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

user_input = input("Enter a list of words separated by spaces: ")
words_list = user_input.split()
word_frequency = count_word_frequency(words_list)

print("\nWord Frequency:")
for word, count in word_frequency.items():
    print(f"{word}: {count}")