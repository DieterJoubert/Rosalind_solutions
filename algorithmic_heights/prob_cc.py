from utils import get_data_from_edge_list_format, build_undirected_graph_from_adjacency_list
from collections import deque

INPUT_PATH = './input/rosalind_cc.txt'

def get_connected_component_coloring(graph):
    coloring = {}
    curr_color = 1

    for x in graph.keys():

        if x in coloring:
            continue

        q = deque()
        q.append(x)

        while q:
            curr_node = q.pop()
            coloring[curr_node] = curr_color

            for neighbor in graph[curr_node]:
                if neighbor not in coloring:
                    q.append(neighbor)

        curr_color += 1

    return coloring

def main():
    num_vertices, num_edges, adjacency_list = get_data_from_edge_list_format(INPUT_PATH)
    graph = build_undirected_graph_from_adjacency_list(num_vertices, adjacency_list)
    coloring = get_connected_component_coloring(graph)
    print(max(coloring.values()))

if __name__ == '__main__':
    main()