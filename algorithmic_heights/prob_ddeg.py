from prob_deg import get_data_from_edge_list_format, build_graph_from_adjacency_list

INPUT_PATH = './input/rosalind_ddeg.txt'
OUTPUT_PATH = './output/prob_ddeg.txt'

def write_solution(double_degrees):
    f = open(OUTPUT_PATH, "w")
    f.write(" ".join(map(str, [double_degrees[n] for n in double_degrees.keys()])))
    f.close()    

def get_double_degrees(graph):
    double_degree = {}

    for node, neighbors in graph.items():
        double_degree[node] = sum([len(graph[n]) for n in neighbors])

    return double_degree

def main():
    num_vertices, num_edges, adjacency_list = get_data_from_edge_list_format(INPUT_PATH)
    graph = build_graph_from_adjacency_list(num_vertices, adjacency_list)
    double_degrees = get_double_degrees(graph)
    write_solution(double_degrees)

if __name__ == '__main__':
    main()