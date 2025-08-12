def translate(text):
    vowels = "aieou"
    result = []
    words = text.split(" ")
    for word in words:
        if word[0] in vowels or word.startswith("xr") or word.startswith("yt"):
            result.append(word + "ay")
            continue
        first_vowel_pos = 0
        for index, letter in enumerate(word):
            if letter == "q":
                if index < (len(word)) - 1 and word[index+1] == "u":
                    result.append(word[index+2:] + word[:index] + "quay")
                    break
            if index > 0 and letter == "y":
                result.append(word[index:] + word[:index] + "ay")
                break
            if letter in vowels:
                first_vowel_pos = index
                result.append(word[first_vowel_pos:] + word[:first_vowel_pos] + "ay")
                break
    return " ".join(result)