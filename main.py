path = "books/"
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

from stats import word_count
from stats import count_characters

def main():
    text = get_book_text("books/frankenstein.txt")
    count = word_count(text)
    print(f"Found {count} total words")
    print(count_characters(contents))
main()
