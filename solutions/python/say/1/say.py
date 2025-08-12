def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    LOOKUP = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    ORDERS = [
        "",
        "thousand",
        "million",
        "billion",
        "trillion",
    ]

    def split_chunks(n):
        chunks = []
        while n > 0:
            chunks.append(n % 1000)
            n //= 1000
        return chunks

    def chunk_to_words(n):
        parts = []

        if n >= 100:
            parts.append(LOOKUP[n // 100] + " hundred")
            n %= 100

        if n >= 20:
            parts.append(LOOKUP[n // 10 * 10])
            if n % 10:
                parts[-1] += "-" + LOOKUP[n % 10]
        elif n > 0:
            parts.append(LOOKUP[n])
        elif not parts:
            parts.append(LOOKUP[0])

        return " ".join(parts)

    if number == 0:
        return LOOKUP[0]

    chunks = split_chunks(number)
    words = []

    for i, chunk in enumerate(chunks):
        if chunk == 0:
            continue
        chunk_words = chunk_to_words(chunk)
        if ORDERS[i]:
            chunk_words += " " + ORDERS[i]
        words.insert(0, chunk_words)

    return " ".join(words)
