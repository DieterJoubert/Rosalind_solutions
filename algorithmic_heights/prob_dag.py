from utils import read_multiple_edge_list_formats, build_directed_graph_from_adjacency_list

INPUT_PATH = './input/rosalind_dag.txt'

def get_topological_sorting():
    pass

def main():
    graphs = read_multiple_edge_list_formats(INPUT_PATH)
    adjacency_lists = [build_directed_graph_from_adjacency_list(g.num_vertices, g.adjacency_list) for g in graphs]
    for x in adjacency_lists:
        print(x)

if __name__ == '__main__':
    main()