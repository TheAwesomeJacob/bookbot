def get_num_words(path_to_file):
    num_words = 0
    dictionary = {}
    list_of_letters = []

    with open(path_to_file) as f:
        num_words += count_words_in_book(f.read())

    with open(path_to_file) as f:
        dictionary = count_letters(f.read(), dictionary)

    for l in dictionary:
        object = {'char': l, 'num': dictionary[l]}
        list_of_letters.append(object)

    list_of_letters.sort(key=sort_by_number, reverse=True)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in list_of_letters:
        print(f"{letter['char']}: {letter['num']}")
    print ("============= END ===============")


def count_words_in_book(text):
    splitted_text = text.split();
    return len(splitted_text)

def count_letters(text, dictionary):
    for w in text:
        if w.isalpha():
            l = w.lower()
            if l in dictionary:
                dictionary[l] += 1
            else:
                dictionary[l] = 1
    return dictionary

def sort_by_number(d):
    return d['num']
