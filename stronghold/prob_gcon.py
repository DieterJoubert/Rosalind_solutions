from utils import get_fasta_data_array, get_blosum62_scoring_matrix

INPUT_PATH = './input/rosalind_gcon.txt'

GAP_PENALTY = -5

def get_penalty(cell, gap_penalty):
    if cell[1] == True:
        return 0
    return gap_penalty

def get_global_alignment_matrix(s: str, t: str, blosum_scoring, gap_penalty: int):
    matrix = [[(0, False) for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    
    for s_idx in range(1, len(s)+1):
        matrix[s_idx][0] = (gap_penalty, True)
    for t_idx in range(1, len(t)+1):
        matrix[0][t_idx] = (gap_penalty, True)

    for s_idx in range(1, len(s)+1):
        for t_idx in range(1, len(t)+1):
            s_symbol = s[s_idx-1]
            t_symbol = t[t_idx-1]

            if s_symbol == t_symbol:
                matrix[s_idx][t_idx] = (matrix[s_idx-1][t_idx-1][0] + blosum_scoring[(s_symbol, t_symbol)], False)
            else:
                choices = [
                    (matrix[s_idx-1][t_idx-1][0] + blosum_scoring[(s_symbol, t_symbol)], False), 
                    (matrix[s_idx][t_idx-1][0] + get_penalty(matrix[s_idx][t_idx-1], gap_penalty), True), 
                    (matrix[s_idx-1][t_idx][0] + get_penalty(matrix[s_idx-1][t_idx], gap_penalty), True)
                ]
                matrix[s_idx][t_idx] = max(choices)

    for row in matrix:
        print(row)

    return matrix

def get_max_alignment_score(matrix):
    return matrix[len(matrix)-1][len(matrix[0])-1][0]

def main():
    s, t = [x[1] for x in get_fasta_data_array(INPUT_PATH)]
    blosum_scoring_matrix = get_blosum62_scoring_matrix()
    global_alignment_matrix = get_global_alignment_matrix(s, t, blosum_scoring_matrix, GAP_PENALTY)
    alignment_score = get_max_alignment_score(global_alignment_matrix)
    print(alignment_score)

if __name__ == '__main__':
    main()