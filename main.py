
def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count_words(file_contents)
    pass

def count_words(text):
    counter = 0
    for i in text.split():
        counter = counter +1
    print(f"{counter} words found in the document")

get_book_text()