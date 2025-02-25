from stats import count_words
from stats import count_letters
import sys

def get_book_text():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_location = sys.argv[1]
    if book_location == None:
        print("No location")
        pass
    with open(book_location) as f:
        file_contents = f.read()
        words = count_words(file_contents)
        letters = count_letters(file_contents)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_location}")
        print("----------- Word Count ----------")
        print(f"Found {words} total words")
        print("--------- Character Count -------")
        for i in letters:
            print(f"{i}: {letters[i]}")
        print("============= END ===============")

get_book_text()