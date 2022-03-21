from utils import get_dna_data, write_solution
from constants import COMPLEMENT_MAP

DATA_PATH = './data/rosalind_revc.txt'
OUTPUT_PATH = './output/prob_revc.txt'

def get_reverse_complement(dna: str) -> str:
    return "".join([COMPLEMENT_MAP[c] for c in dna[::-1]])

def main():
    data = get_dna_data(DATA_PATH)
    revc = get_reverse_complement(data)
    write_solution(OUTPUT_PATH, [revc])

if __name__ == '__main__':
    main()