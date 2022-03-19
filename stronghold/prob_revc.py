from utils import get_dna_data, write_solution
from constants import COMPLEMENT_MAP

def get_reverse_complement(dna: str) -> str:
    return "".join([COMPLEMENT_MAP[c] for c in dna[::-1]])

def main():
    data = get_dna_data('./data/rosalind_revc.txt')
    revc = get_reverse_complement(data)
    write_solution('./output/prob_revc.txt', [revc])

if __name__ == '__main__':
    main()