from stats import count_words

def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count_words(file_contents)
    pass

get_book_text()