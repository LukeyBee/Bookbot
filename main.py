path = "books/"
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

from stats import book_splitter
from stats import word_count
from stats import letter_count

def main():
    text = get_book_text("books/frankenstein.txt")
    words = book_splitter(text)
    total_words = word_count(words)
    characters = letter_count(text)
    print(f"Found {total_words} total words")
    print(characters)
main()
