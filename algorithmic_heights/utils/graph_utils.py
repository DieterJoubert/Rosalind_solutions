class EdgeListData:
    def __init__(self, num_vertices: int, num_edges: int, adjacency_list):
        self.num_vertices = num_vertices
        self.num_edges = num_edges
        self.adjacency_list = adjacency_list

def get_data_from_edge_list_format(src):
    with open(src) as f:
        lines = f.read().splitlines()
        num_vertices, num_edges = map(int, lines[0].split())
        adjacency_list = [tuple(map(int, line.split())) for line in lines[1:]]
        return num_vertices, num_edges, adjacency_list

def read_multiple_edge_list_formats(src):
    with open(src) as f:
        lines = f.read().splitlines()[2:]

        raw_graphs = [[]]

        for line in lines:
            if not line:
                raw_graphs.append([])
            else:
                raw_graphs[-1].append(line)

        graphs = []

        for raw_graph in raw_graphs:
            num_vertices, num_edges = map(int, raw_graph[0].split())
            adjacency_list = [tuple(map(int, line.split())) for line in raw_graph[1:]]
            graphs.append(EdgeListData(num_vertices, num_edges, adjacency_list))

        return graphs
        
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
