from utils import get_fasta_data

DATA_SRC = './data/rosalind_grph.txt'
OUTPUT_SRC = './output/prob_grph.txt'
k = 3

def get_overlap_graph_adjacency_list(data):
    adjacency_list = []

    for (id1, dna1) in data.items():
        for (id2, dna2) in data.items():
            if id1 == id2:
                continue
            
            if dna1[-k:] == dna2[:k]:
                adjacency_list.append((id1, id2))
    
    return adjacency_list

def write_solution(adjacency_list):
    f = open(OUTPUT_SRC, "w")
    f.writelines(map(lambda x: " ".join(x) + "\n", adjacency_list))
    f.close()

def main():
    data = get_fasta_data(DATA_SRC)
    adjacency_list = get_overlap_graph_adjacency_list(data)
    write_solution(adjacency_list)

if __name__ == '__main__':
    main()