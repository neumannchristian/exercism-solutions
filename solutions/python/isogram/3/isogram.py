def is_isogram(string):
    seen = set()
    return not any(
        letter.lower() in seen or seen.add(letter.lower())
        for letter in string
        if letter.isalpha()
    )