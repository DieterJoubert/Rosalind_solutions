from utils import get_fasta_data

DATA_SRC = './data/rosalind_long.txt'
OUTPUT_SRC = './output/prob_long.txt'

def get_overlap(dna1, dna2):
    min_length = min(len(dna1), len(dna2))

    best_overlap = 0

    for i in range(min_length // 2, min_length):
        if dna1[-i:] == dna2[:i]:
            best_overlap = i

    return best_overlap

def get_superstring(dna_strings):
    strings_left = set(dna_strings[1:])

    super = dna_strings[0]

    while strings_left:
        best = (0, None, None)

        for s in strings_left:
            append_overlap = get_overlap(super, s)
            prepend_overlap = get_overlap(s, super)
            
            possible = (append_overlap, s, 'append') if append_overlap >= prepend_overlap else (prepend_overlap, s, 'prepend')

            if possible[0] > best[0]:
                best = possible

        if best[2] == 'append':
            super = super + best[1][best[0]:]
        elif best[2] == 'prepend':
            super = best[1][:-best[0]] + super
        else:
            raise Exception()

        strings_left.remove(best[1])        

    return super

def write_solution(superstring):
    f = open(OUTPUT_SRC, "w")
    f.write(superstring)
    f.close()

def main():
    data = get_fasta_data(DATA_SRC)
    superstring = get_superstring(list(data.values()))
    write_solution(superstring)

if __name__ == '__main__':
    main()