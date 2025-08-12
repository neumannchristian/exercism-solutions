from string import ascii_lowercase, ascii_uppercase

def rotate(text, key):
    result = []
    for char in text:
        if char.islower():
            pos = ascii_lowercase.index(char)
            result.append(ascii_lowercase[(pos + key) % 26])
        elif char.isupper():
            pos = ascii_uppercase.index(char)
            result.append(ascii_uppercase[(pos + key) % 26])
        else:
            result.append(char)
    return "".join(result)