from utils import get_data_from_edge_list_format, build_directed_graph_from_adjacency_list
from collections import deque

INPUT_PATH = './input/rosalind_bfs.txt'
OUTPUT_PATH = './output/prob_bfs.txt'

def write_solution(shortest_paths):
    f = open(OUTPUT_PATH, "w")
    f.write(" ".join(map(str, [shortest_paths[n] for n in shortest_paths.keys()])))
    f.close()    

def get_shortest_path_from(graph, node=1):
    shortest_paths = {n: -1 for n in graph.keys()}
    explored = set()

    q = deque()
    q.append((node, 0))

    while q:
        (curr_node, curr_length) = q.popleft()

        explored.add(curr_node)
        shortest_paths[curr_node] = min(shortest_paths[curr_node], curr_length) if shortest_paths[curr_node] != -1 else curr_length

        for neighbor in graph[curr_node]:
            if neighbor not in explored:
                q.append((neighbor, curr_length+1))

    return shortest_paths

def main():
    num_vertices, num_edges, adjacency_list = get_data_from_edge_list_format(INPUT_PATH)
    graph = build_directed_graph_from_adjacency_list(num_vertices, adjacency_list)
    shortest_paths = get_shortest_path_from(graph)
    write_solution(shortest_paths)

if __name__ == '__main__':
    main()