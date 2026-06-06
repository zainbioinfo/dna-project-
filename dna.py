dna = "ATGCGATACG"

print("DNA Sequence:", dna)

gc = (dna.count("G") + dna.count("C")) / len(dna) * 100
print("GC Content:", gc)
