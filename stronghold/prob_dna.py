from constants import VALID_DNA_SYMBOLS

def get_data() -> str:
    with open('./data/rosalind_dna.txt') as f:
        lines = f.read().splitlines()
        return lines[0]

def get_dna_counts(dna: str) -> 'dict[str, int]':
    counts = {c: 0 for c in VALID_DNA_SYMBOLS}

    for c in dna:
        if c not in VALID_DNA_SYMBOLS:
            raise Exception(f'Character "{c}" is not valid')
        counts[c] += 1

    return counts

def get_output(counts: 'dict[str, int]'):
    values = [counts[i] for i in sorted(counts.keys())]
    return " ".join(map(lambda x: str(x), values))

def main():
    data = get_data()
    counts = get_dna_counts(data)
    output = get_output(counts)
    print(output)

if __name__ == '__main__':
    main()