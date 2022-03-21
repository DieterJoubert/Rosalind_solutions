from utils import get_data_from_edge_list_format, build_undirected_graph_from_adjacency_list

INPUT_PATH = './input/rosalind_deg.txt'
OUTPUT_PATH = './output/prob_deg.txt'

def write_solution(graph):
    f = open(OUTPUT_PATH, "w")
    f.write(" ".join(map(str, [len(graph[n]) for n in graph.keys()])))
    f.close()    

def main():
    num_vertices, num_edges, adjacency_list = get_data_from_edge_list_format(INPUT_PATH)
    graph = build_undirected_graph_from_adjacency_list(num_vertices, adjacency_list)
    write_solution(graph)

if __name__ == '__main__':
    main()