def is_isogram(string):
    collection = []
    for letter in string:
        if letter.lower() in collection and letter.isalpha():
            return False
        if letter.isalpha():
            collection.append(letter.lower())
    return True