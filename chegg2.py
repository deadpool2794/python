


def get_words(my_sentence):
    # Using split() method to split the given sentence into a list
    words = my_sentence.split()
    # Initializing a set to store unique words
    unique_words = set()
    for word in words:
        # Converting the word to lowercase
        word = word.lower()
        required_word = ''
        # Iterating throung each character of the word and making sure
        # that the word to be added does not contain any punctuation
        for i in word:
            if (i >= '0' and i <= '9') or (i >= 'a' and i <= 'z'):
                required_word += i
        unique_words.add(required_word)
    return list(unique_words)




my_sentence = "Grocery list:    3 boxes Land-o-Lakes butter, Aunt Jemima's butter pancake mix"

words = get_words(my_sentence)
print(words)
for i in words:
    print(i)