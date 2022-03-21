from utils import get_fasta_data_array

INPUT_PATH = './input/rosalind_pdst.txt'
OUTPUT_PATH = './output/prob_pdst.txt'

def write_solution(distance_matrix):
    f = open(OUTPUT_PATH, "w")
    for row in distance_matrix:
        f.write(" ".join(map(str, row)) + "\n")
    f.close()

def get_difference_percentage(s, t):
    if len(s) != len(t):
        raise Exception("Strings are not the same length")

    diff_count = 0

    for i in range(len(s)):
        if s[i] != t[i]:
            diff_count += 1

    return diff_count / len(s)

def get_distance_matrix(dna_strings):
    matrix = [[0 for _ in range(len(dna_strings))] for _ in range(len(dna_strings))]

    for i in range(len(dna_strings)):
        for j in range(len(dna_strings)):
            s = dna_strings[i]
            t = dna_strings[j]
            matrix[i][j] = get_difference_percentage(s, t)

    return matrix
            
def main():
    data = get_fasta_data_array(INPUT_PATH)
    distance_matrix = get_distance_matrix([x[1] for x in data])
    write_solution(distance_matrix)

if __name__ == '__main__':
    main()