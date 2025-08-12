ENCODE_TABLE = str.maketrans("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba")
DECODE_TABLE = str.maketrans("zyxwvutsrqponmlkjihgfedcba", "abcdefghijklmnopqrstuvwxyz")


def encode(plain_text):
    filtered = "".join(
        [
            letter
            for letter in plain_text.lower().translate(ENCODE_TABLE)
            if letter.isalnum()
        ]
    )
    return " ".join([filtered[i : i + 5] for i in range(0, len(filtered), 5)])


def decode(ciphered_text):
    return ciphered_text.lower().replace(" ", "").translate(DECODE_TABLE)
