def book_splitter(file_contents):
    return file_contents.split()

def word_count(word):
    return len(word)

def letter_count(book_words):
    letters_dict = {}
    words = book_words.lower()
    for letter in words:
        if letter not in letters_dict:
            letters_dict[letter] = 1
        else:
            letters_dict[letter] += 1
    return letters_dict
