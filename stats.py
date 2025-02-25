def count_words(text):
    counter = 0
    for i in text.split():
        counter = counter +1
    return counter
    #print(f"{counter} words found in the document")

def sort_on():
    return dict.values()

def count_letters(book):
    letters = {'t':0}
    for i in book:
        l_letter= i.lower()
        if l_letter not in letters and l_letter.isalpha() == True:
            letters[l_letter] = l_letter
            letters[l_letter] = 1
        elif l_letter in letters and l_letter.isalpha() == True:
            letters[l_letter] += 1
    sorted_letters = dict(sorted(letters.items(),key=lambda item: item[1], reverse=True))
    return(sorted_letters)