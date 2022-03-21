from utils import get_fasta_data

INPUT_PATH = './input/rosalind_lcsq.txt'

def get_lcs_matrix(s, t):
    matrix = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]

    for i_s in range(len(s)):
        for i_t in range(len(t)):
            x, y = i_s + 1, i_t + 1
            if s[i_s] == t[i_t]:
                matrix[x][y] = matrix[x-1][y-1] + 1
            else:
                matrix[x][y] = max(matrix[x][y-1], matrix[x-1][y])

    return matrix

def get_subsequence_from_matrix(s, t, matrix):
    result = ''
    x, y = (len(matrix)-1, len(matrix[0])-1)

    while True:
        if matrix[x][y] > matrix[x-1][y-1] and matrix[x][y] > matrix[x][y-1] and matrix[x][y] > matrix[x-1][y]:
            if s[x-1] != t[y-1]:
                raise Exception()
            result = s[x-1] + result
            x -= 1
            y -= 1
        elif matrix[x-1][y] > matrix[x][y-1]:
            x -= 1
        else:
            y -=1 

        if x == 0 or y == 0:
            break

    return result

def main():
    dna_strings = list(get_fasta_data(INPUT_PATH).values())
    s, t = dna_strings
    lcs_matrix = get_lcs_matrix(s, t)
    lcs = get_subsequence_from_matrix(s, t, lcs_matrix)
    print(lcs)

if __name__ == '__main__':
    main()