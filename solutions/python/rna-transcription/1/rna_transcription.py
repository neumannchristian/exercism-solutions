def to_rna(dna_strand):
    conversion_table = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }
    return "".join(
        conversion_table.get(nucleotide) for nucleotide in list(dna_strand)
    )
