from utils import get_monoisotopic_mass_table

DATA_PATH = './data/rosalind_prtm.txt'

def get_data():
    with open(DATA_PATH) as f:
        lines = f.read().splitlines()
        return lines[0]

def get_total_weight(protein, mass_table):
    return sum([mass_table[x] for x in protein])

def main():
    protein = get_data()
    mass_table = get_monoisotopic_mass_table()
    total_weight = get_total_weight(protein, mass_table)
    print(total_weight)

if __name__ == '__main__':
    main()