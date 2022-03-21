def get_data_from_edge_list_format(src):
    with open(src) as f:
        lines = f.read().splitlines()
        num_vertices, num_edges = map(int, lines[0].split())
        adjacency_list = [tuple(map(int, line.split())) for line in lines[1:]]
        return num_vertices, num_edges, adjacency_list

def build_graph_from_adjacency_list(num_vertices, adj_list, directed=False):
    graph = {n: [] for n in range(1, num_vertices+1)}

    for (x,y) in adj_list:
        graph[x].append(y)
        if not directed:
            graph[y].append(x)

    return graph

def build_undirected_graph_from_adjacency_list(num_vertices, adj_list):
    return build_graph_from_adjacency_list(num_vertices, adj_list, directed=False)

def build_directed_graph_from_adjacency_list(num_vertices, adj_list):
    return build_graph_from_adjacency_list(num_vertices, adj_list, directed=True)
