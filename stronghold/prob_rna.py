DATA_PATH = './data/rosalind_rna.txt'
OUTPUT_PATH = './output/prob_rna.txt'

def get_data() -> str:
    with open(DATA_PATH) as f:
        lines = f.read().splitlines()
        return lines[0]

def convert_dna_to_rna(dna: str) -> str:
    return dna.replace('T', 'U')

def write_solution(rna: str):
    f = open(OUTPUT_PATH, "w")
    f.write(rna)
    f.close()

def main():
    data = get_data()
    rna = convert_dna_to_rna(data)
    write_solution(rna)

if __name__ == '__main__':
    main()