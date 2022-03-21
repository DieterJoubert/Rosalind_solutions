from utils import get_fasta_data_array

DATA_PATH = './data/rosalind_edit.txt'

def get_edit_distance_matrix(s, t):
    matrix = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    
    for s_idx in range(len(s)+1):
        matrix[s_idx][0] = s_idx
    for t_idx in range(len(t)+1):
        matrix[0][t_idx] = t_idx

    for s_idx in range(1, len(s)+1):
        for t_idx in range(1, len(t)+1):
            if s[s_idx-1] == t[t_idx-1]:
                matrix[s_idx][t_idx] = matrix[s_idx-1][t_idx-1]
            else:
                matrix[s_idx][t_idx] = 1 + min(matrix[s_idx-1][t_idx-1], matrix[s_idx][t_idx-1], matrix[s_idx-1][t_idx])

    return matrix

def get_edit_distance_from_matrix(edit_matrix):
    return edit_matrix[len(edit_matrix)-1][len(edit_matrix[0])-1]

def main():
    s, t = [x[1] for x in get_fasta_data_array(DATA_PATH)]
    edit_matrix = get_edit_distance_matrix(s, t)
    edit_distance = get_edit_distance_from_matrix(edit_matrix)
    print(edit_distance)

if __name__ == '__main__':
    main()