import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path = sys.argv[1]
from stats import book_splitter
from stats import word_count
from stats import letter_count
from stats import dict_sort

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    text = get_book_text(path)
    words = book_splitter(text)
    total_words = word_count(words)
    characters = letter_count(text)
    book_report = dict_sort(characters)
    print(f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {total_words} total words
--------- Character Count -------""")
    for item in book_report:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()
