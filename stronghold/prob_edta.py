from utils import get_fasta_data_array
from prob_edit import get_edit_distance_matrix, get_edit_distance_from_matrix

DATA_PATH = './data/rosalind_edta.txt'
OUTPUT_PATH = './output/prob_edta.txt'

def get_optimal_alignments(s, t, matrix):
    s_aligned, t_aligned = '', ''

    s_idx, t_idx = (len(s), len(t))
    
    while True:
        action = None

        if s_idx == 0 and t_idx == 0:
            action = 'end'
        elif s_idx == 0:
            action = 'left'
        elif t_idx == 0:
            action = 'up'
        else:
            options = {
                'diag': matrix[s_idx-1][t_idx-1], 
                'left': matrix[s_idx][t_idx-1], 
                'up': matrix[s_idx-1][t_idx]
            }
            action = min(options, key=options.get)

        if action == 'end':
            break
        elif action == 'diag':
            s_aligned = s[s_idx-1] + s_aligned
            t_aligned = t[t_idx-1] + t_aligned
            s_idx -= 1
            t_idx -= 1
        elif action == 'left':
            s_aligned = '-' + s_aligned
            t_aligned = t[t_idx-1] + t_aligned
            t_idx -= 1
        elif action == 'up':
            s_aligned = s[s_idx-1] + s_aligned
            t_aligned = '-' + t_aligned
            s_idx -= 1

    return s_aligned, t_aligned

def write_solution(edit_distance: int, s_aligned: str, t_aligned: str):
    f = open(OUTPUT_PATH, "w")
    f.write(str(edit_distance) + "\n")
    f.write(s_aligned + "\n")
    f.write(t_aligned + "\n")
    f.close()

def main():
    s, t = [x[1] for x in get_fasta_data_array(DATA_PATH)]
    edit_matrix = get_edit_distance_matrix(s, t)
    edit_distance = get_edit_distance_from_matrix(edit_matrix)
    s_aligned, t_aligned = get_optimal_alignments(s, t, edit_matrix)
    write_solution(edit_distance, s_aligned, t_aligned)

if __name__ == '__main__':
    main()