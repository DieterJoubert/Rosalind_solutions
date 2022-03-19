from utils import get_fasta_data
from prob_lexf import get_permutations
from constants import VALID_DNA_SYMBOLS

DATA_SRC = './data/rosalind_kmer.txt'
OUTPUT_SRC = './output/prob_kmer.txt'

k = 4

def write_solution(perms):
    f = open(OUTPUT_SRC, "w")
    for perm in perms:
        f.write(perm + "\n")
    f.close()

def get_kmers(k):
    return sorted(get_permutations(VALID_DNA_SYMBOLS, k))

def get_kmer_composition(k, dna, kmers):
    kmer_to_index = {kmers[i]: i for i in range(len(kmers))}
    composition = [0] * len(kmers)

    for i in range(len(dna)-k+1):
        segment = dna[i:i+k]
        index = kmer_to_index[segment]
        composition[index] += 1

    return composition

def write_solution(composition):
    f = open(OUTPUT_SRC, "w")
    f.write(" ".join(map(lambda x: str(x), composition)))
    f.close()

def main():
    data = get_fasta_data(DATA_SRC)
    dna = list(data.values())[0]
    kmers = get_kmers(k)
    composition = get_kmer_composition(k, dna, kmers)
    write_solution(composition)

if __name__ == '__main__':
    main()