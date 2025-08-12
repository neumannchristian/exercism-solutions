import re

def response(hey_bob):
    hey_bob = hey_bob.strip()
    if not hey_bob:
        return "Fine. Be that way!"
    if hey_bob.isupper() and hey_bob[-1] == "?":
        return "Calm down, I know what I'm doing!"
    elif hey_bob[-1] == "?":
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    return "Whatever."
