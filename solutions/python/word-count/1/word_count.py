import re


def count_words(sentence):
    words = re.findall(
        r"(\b[a-z0-9]+'?[a-z0-9]*)\b", sentence.lower().replace("_", " ")
    )

    tally = {}
    for word in words:
        if tally.get(word):
            tally[word] += 1
        else:
            tally.setdefault(word, 1)

    return tally
