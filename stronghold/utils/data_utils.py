from typing import List

CODON_TABLE_SRC = './data/rna_codon_table.txt'
MONOISOTOPIC_MASS_TABLE_SRC = './data/monoisotopic_mass_table.txt'
BLOSUM_PATH = './data/blosum62.txt'

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

def get_monoisotopic_mass_table():
    table = {}
    with open(MONOISOTOPIC_MASS_TABLE_SRC) as f:
        lines = map(lambda x: x.split(), f.read().splitlines())
        for line in lines:
            table[line[0]] = float(line[1])
    return table


def get_blosum62_scoring_matrix():
    matrix = {}
    with open(BLOSUM_PATH) as f:
        lines = f.read().splitlines()
        header = lines[0].split()
        content = [line.split()[1:] for line in lines[1:]]
        for i in range(len(header)):
            for j in range(len(header)):
                matrix[(header[i], header[j])] = int(content[i][j])
        return matrix

def get_fasta_data(src: str):
    data = {}

    with open(src) as f:
        lines = f.read().splitlines()

        curr_id = None

        for line in lines:
            if line[0] == '>':
                curr_id = line[1:]
                data[curr_id] = ''
            else:
                data[curr_id] += line

    return data

def get_fasta_data_array(src: str):
    data = []

    with open(src) as f:
        lines = f.read().splitlines()

        for line in lines:
            if line[0] == '>':
                id = line[1:]
                data.append([id, ''])
            else:
                data[-1][1] += line

    return data