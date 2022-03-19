from utils import get_fasta_data
from constants import VALID_DNA_SYMBOLS

DATA_SRC = './data/rosalind_cons.txt'

def get_profile(data):
    dna_length = len(list(data.values())[0])
    profile = {x: [0] * dna_length for x in VALID_DNA_SYMBOLS}

    for (_, dna) in data.items():
        for i in range(len(dna)):
            c = dna[i]
            profile[c][i] += 1

    return profile

def get_consensus(profile):
    consensus = ''

    for i in range(len(list(profile.values())[0])):
        best = (None, 0)

        for symbol in VALID_DNA_SYMBOLS:
            count = profile[symbol][i]
            if count > best[1]:
                best = (symbol, count)

        consensus += best[0]

    return consensus

def write_solution(profile, consensus):
    f = open("./output/prob_cons.txt", "w")
    f.write(consensus + '\n')
    for c in VALID_DNA_SYMBOLS:
        count_str = " ".join(map(lambda x: str(x), profile[c]))
        f.write(f'{c}: {count_str} \n')
    f.close()

def main():
    data = get_fasta_data(DATA_SRC)
    profile = get_profile(data)
    consensus = get_consensus(profile)
    write_solution(profile, consensus)

if __name__ == '__main__':
    main()