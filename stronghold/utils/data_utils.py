from typing import List

CODON_TABLE_SRC = './data/rna_codon_table.txt'

def get_dna_data(src: str) -> str:
    with open(src) as f:
        lines = f.read().splitlines()
        return lines[0]

def write_solution(destination: str, content: List[str]):
    f = open(destination, "w")
    for c in content:
        f.write(c)
    f.close()

def get_codon_table():
    table = {}
    with open(CODON_TABLE_SRC) as f:
        lines = map(lambda x: x.split(), f.read().splitlines())
        for line in lines:
            for idx in range(len(line)):
                if idx % 2 != 0:
                    continue
                table[line[idx]] = line[idx+1]
    return table