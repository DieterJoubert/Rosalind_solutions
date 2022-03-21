from utils import get_fasta_data_array

DATA_PATH = './data/rosalind_glob.txt'
BLOSUM_PATH = './data/blosum62.txt'
OUTPUT_PATH = './output/prob_glob.txt'

GAP_PENALTY = -5

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

def get_global_alignment_matrix(s: str, t: str, blosum_scoring, gap_penalty: int):
    matrix = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    
    for s_idx in range(len(s)+1):
        matrix[s_idx][0] = s_idx * gap_penalty
    for t_idx in range(len(t)+1):
        matrix[0][t_idx] = t_idx * gap_penalty

    for s_idx in range(1, len(s)+1):
        for t_idx in range(1, len(t)+1):
            s_symbol = s[s_idx-1]
            t_symbol = t[t_idx-1]

            if s_symbol == t_symbol:
                matrix[s_idx][t_idx] = matrix[s_idx-1][t_idx-1] + blosum_scoring[(s_symbol, t_symbol)]
            else:
                matrix[s_idx][t_idx] = max(matrix[s_idx-1][t_idx-1] + blosum_scoring[(s_symbol, t_symbol)], 
                                            matrix[s_idx][t_idx-1] + gap_penalty, 
                                            matrix[s_idx-1][t_idx] + gap_penalty)

    return matrix

def get_max_alignment_score(matrix):
    return matrix[len(matrix)-1][len(matrix[0])-1]

def main():
    s, t = [x[1] for x in get_fasta_data_array(DATA_PATH)]
    blosum_scoring_matrix = get_blosum62_scoring_matrix()
    global_alignment_matrix = get_global_alignment_matrix(s, t, blosum_scoring_matrix, GAP_PENALTY)
    alignment_score = get_max_alignment_score(global_alignment_matrix)
    print(alignment_score)

if __name__ == '__main__':
    main()