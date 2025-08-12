from string import ascii_lowercase

ENCODE_TABLE = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])
DECODE_TABLE = str.maketrans(ascii_lowercase[::-1], ascii_lowercase)


def encode(plain_text: str):
    filtered = "".join(chr for chr in plain_text.lower() if chr.isalnum()).translate(
        ENCODE_TABLE
    )
    return " ".join([filtered[idx : idx + 5] for idx in range(0, len(filtered), 5)])


def decode(ciphered_text: str):
    return ciphered_text.lower().replace(" ", "").translate(DECODE_TABLE)
