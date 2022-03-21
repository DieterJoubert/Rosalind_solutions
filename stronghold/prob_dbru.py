from prob_revc import get_reverse_complement

INPUT_PATH = './input/rosalind_dbru.txt'
OUTPUT_PATH = './output/prob_dbru.txt'

def get_data():
    with open(INPUT_PATH) as f:
        lines = f.read().splitlines()
        return lines

def get_k_plus_one_set(k_plus_one_mers):
    k_plus_one_set = set(k_plus_one_mers)

    for item in k_plus_one_mers:
        k_plus_one_set.add(get_reverse_complement(item))

    return k_plus_one_set

def get_debruijn_adjacency_list(k_plus_one_set):
    adj_list = set()

    for k1 in k_plus_one_set:
        seg1 = k1[:-1]
        seg2 = k1[1:]
        
        adj_list.add((seg1, seg2))

    return sorted(list(adj_list))

def write_solution(adjacency_list):
    f = open(OUTPUT_PATH, "w")
    for item in adjacency_list:
        f.write(f'({item[0]}, {item[1]}) \n')
    f.close()

def main():
    k_plus_one_mers = get_data()
    k_plus_one_set = get_k_plus_one_set(k_plus_one_mers)
    
    adj_list = get_debruijn_adjacency_list(k_plus_one_set)
    
    write_solution(adj_list)

if __name__ == '__main__':
    main()