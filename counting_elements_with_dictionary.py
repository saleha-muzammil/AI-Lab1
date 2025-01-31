def count_word_frequency(list_of_word):
    word_freq = {}
    for word in list_of_word:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

def main():
    list_of_word = ""
    print("Enter the list of words: ")
    while True:
        word = input()
        if word == "" or word == "\n":
            break
        list_of_word += (word)
    
    word_freq = count_word_frequency(list_of_word.split())
    print("Word frequency: ")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()