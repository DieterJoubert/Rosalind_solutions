
INPUT_PATH = './input/rosalind_deg.txt'
OUTPUT_PATH = './output/prob_deg.txt'

def get_data_from_edge_list_format(src):
    with open(src) as f:
        lines = f.read().splitlines()
        num_vertices, num_edges = map(int, lines[0].split())
        adjacency_list = [tuple(map(int, line.split())) for line in lines[1:]]
        return num_vertices, num_edges, adjacency_list

def build_graph_from_adjacency_list(num_vertices, adj_list):
    graph = {n: [] for n in range(1, num_vertices+1)}

    for (x,y) in adj_list:
        graph[x].append(y)
        graph[y].append(x)

    return graph

def write_solution(graph):
    f = open(OUTPUT_PATH, "w")
    f.write(" ".join(map(str, [len(graph[n]) for n in graph.keys()])))
    f.close()    

def main():
    num_vertices, num_edges, adjacency_list = get_data_from_edge_list_format(INPUT_PATH)
    graph = build_graph_from_adjacency_list(num_vertices, adjacency_list)
    write_solution(graph)

if __name__ == '__main__':
    main()