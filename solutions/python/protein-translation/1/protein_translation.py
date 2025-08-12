LOOKUP = {
    "Methionine": ("AUG"),
    "Phenylalanine": ("UUU", "UUC"),
    "Leucine": ("UUA", "UUG"),
    "Serine": ("UCU", "UCC", "UCA", "UCG"),
    "Tyrosine": ("UAU", "UAC"),
    "Cysteine": ("UGU", "UGC"),
    "Tryptophan": ("UGG"),
    "STOP": ("UAA", "UAG", "UGA"),
}


def proteins(strand):
    result = []
    for idx in range(0, len(strand), 3):
        codon = strand[idx : idx + 3]
        if codon in LOOKUP["STOP"]:
            return result
        for protein, codons in LOOKUP.items():
            if codon in codons:
                result.append(protein)
    return result
