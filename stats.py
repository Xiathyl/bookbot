def count_words(text):
    counter = 0
    for i in text.split():
        counter = counter +1
    print(f"{counter} words found in the document")