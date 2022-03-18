from typing import Dict
from utils import get_codon_table, get_dna_data

def translate_rna_to_protein(rna: str, codon_table: Dict[str, str]):
    protein = ''

    for idx in range(len(rna)):
        if idx % 3 != 0:
            continue
        codon = rna[idx:idx+3]
        amino_acid = codon_table[codon]
        if amino_acid == 'Stop':
            break

        protein += amino_acid
    
    return protein

def main():
    data = get_dna_data('./data/rosalind_prot.txt')
    codon_table = get_codon_table()
    protein = translate_rna_to_protein(data, codon_table)
    print(protein)

if __name__ == '__main__':
    main()