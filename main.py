path = "books/"
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
contents = ()
def word_count(file_contents):
    contents = file_contents.split()
    return len(contents)

def main():
    text = get_book_text("books/frankenstein.txt")
    count = word_count(text)
    print(f"{count} words found in the document")
main()
