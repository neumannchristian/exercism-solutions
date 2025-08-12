def find_anagrams(word, candidates):

    def count_letters(word):
        counts = {}
        for letter in [*word.lower()]:
            counts[letter] = counts.setdefault(letter, 0)+1
        return counts

    master = count_letters(word)

    anagrams = []
    for candidate in candidates:
        
        candidate_letter_counts = count_letters(candidate)
        if candidate_letter_counts == master and not candidate.lower() == word.lower():
            anagrams.append(candidate)
    return anagrams
