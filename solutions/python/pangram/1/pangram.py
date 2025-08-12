def is_pangram(sentence):
    letters = {letter.lower() for letter in sentence if letter.isalpha()}
    return True if len(letters) == 26 else False