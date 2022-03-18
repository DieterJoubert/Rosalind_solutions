from typing import List

def get_data() -> str:
    with open('./data/rosalind_hamm.txt') as f:
        lines = f.read().splitlines()
        return lines

def get_hamming_distance(dna_strings: List[str]) -> int:
    distance = 0

    if len(dna_strings[0]) != len(dna_strings[1]):
        raise Exception("DNA strings not the same length")

    for (c1, c2) in zip(dna_strings[0], dna_strings[1]):
        if c1 != c2:
            distance += 1

    return distance

def main():
    data = get_data()
    hamming_distance = get_hamming_distance(data)
    print(hamming_distance)

if __name__ == '__main__':
    main()