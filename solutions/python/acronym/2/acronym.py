def abbreviate(words):
    phrase = words.replace("-", " ").replace("_", " ").upper().split()
    acronym = ""
    for word in phrase:
        acronym += word[0]
    return acronym
