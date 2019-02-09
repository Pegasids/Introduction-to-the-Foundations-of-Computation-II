def all_words(word):
    
    words = set()
    if len(word) == 1:
        # base case:
        words.add(word)
    else:
        # recursive case:
        for i in range(len(word)):
            for string in all_words(word[:i] + word[i+1:]):
                words.add(word[i] + string)
    
    
    
    
    
    return words

def main():
    word = input("Input word: ")
    print(all_words(word))

if __name__ == "__main__":
    main()
