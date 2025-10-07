def book_splitter(file_contents):
    return file_contents.split()

def word_count(word):
    return len(word)

def letter_count(book_words):
    letters_dict = {}
    words = book_words.lower()
    for letter in words:
        if letter.isalpha() == True:
            if letter not in letters_dict:
                letters_dict[letter] = 1
            else:
                letters_dict[letter] += 1
    return letters_dict

def sort_on(items):
    return items["num"]

def dict_sort(dictionary):
    dict_list = []
    for char, num in dictionary.items():
        dict_list.append({"char": char, "num": num})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list