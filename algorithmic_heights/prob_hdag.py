from utils import read_multiple_edge_list_formats, build_directed_graph_from_adjacency_list
from prob_dag import get_reverse_graph, get_source_nodes, get_topological_sorting

INPUT_PATH = './input/rosalind_hdag.txt'
OUTPUT_PATH = './output/prob_hdag.txt'

def write_solution(array):
    f = open(OUTPUT_PATH, "w")
    for item in array:
        if not item:
            f.write("-1")
        else:
            f.write(" ".join(map(str, [1] + item)))
        f.write("\n")
    f.close()

def get_hamiltonian_path(graph):
    reverse_graph = get_reverse_graph(graph)
    source_nodes = get_source_nodes(reverse_graph)
    topological_sorting = get_topological_sorting(graph, reverse_graph, source_nodes)

    if not topological_sorting:
        return None

    for idx in range(len(topological_sorting)-1):
        node_1, node_2 = topological_sorting[idx], topological_sorting[idx+1]

        if node_2 not in graph[node_1]:
            return False

    return topological_sorting


def main():
    edge_lists = read_multiple_edge_list_formats(INPUT_PATH)
    graphs = [build_directed_graph_from_adjacency_list(g.num_vertices, g.adjacency_list) for g in edge_lists]
    hamiltion_paths_for_graphs = [get_hamiltonian_path(g) for g in graphs]
    write_solution(hamiltion_paths_for_graphs)

if __name__ == '__main__':
    main()