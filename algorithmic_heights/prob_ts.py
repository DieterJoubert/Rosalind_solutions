from utils import get_data_from_edge_list_format, build_directed_graph_from_adjacency_list
from prob_dag import get_reverse_graph, get_source_nodes, get_topological_sorting

INPUT_PATH = './input/rosalind_ts.txt'
OUTPUT_PATH = './output/prob_ts.txt'

def write_solution(array):
    f = open(OUTPUT_PATH, "w")
    f.write(" ".join(map(str, array)))
    f.close()

def main():
    num_vertices, num_edges, adjacency_list = get_data_from_edge_list_format(INPUT_PATH)
    graph = build_directed_graph_from_adjacency_list(num_vertices, adjacency_list)
    reverse_graph = get_reverse_graph(graph)
    source_nodes = get_source_nodes(reverse_graph)
    topological_sorting = get_topological_sorting(graph, reverse_graph, source_nodes)
    write_solution(topological_sorting)

if __name__ == '__main__':
    main()