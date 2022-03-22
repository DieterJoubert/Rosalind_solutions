from utils import read_multiple_edge_list_formats, build_directed_graph_from_adjacency_list

INPUT_PATH = './input/rosalind_dag.txt'
OUTPUT_PATH = './output/prob_dag.txt'

def write_solution(array):
    f = open(OUTPUT_PATH, "w")
    f.write(" ".join(map(lambda x: "1" if x else "-1", array)))
    f.close()

def get_reverse_graph(graph):
    reverse_graph = {n: [] for n in graph.keys()}

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            reverse_graph[neighbor].append(node)

    return reverse_graph

def get_source_nodes(node_to_incoming_neighbor):
    return [node for (node, incoming_neighbors) in node_to_incoming_neighbor.items() if not incoming_neighbors]

def get_topological_sorting(graph, reverse_graph, source_nodes):
    topological_sorting = []
    S = set(source_nodes)

    while S:
        n = S.pop()
        topological_sorting.append(n)

        neighbors = [x for x in graph[n]]

        for m in neighbors:
            graph[n].remove(m)
            reverse_graph[m].remove(n)

            if not reverse_graph[m]:
                S.add(m)

    if any([len(graph[n]) > 0 for n in graph.keys()]):
        return None
    else:
        return topological_sorting

def is_acyclic(graph):
    reverse_graph = get_reverse_graph(graph)
    source_nodes = get_source_nodes(reverse_graph)
        
    if not source_nodes:
        return False

    topological_sorting = get_topological_sorting(graph, reverse_graph, source_nodes)
    return True if topological_sorting else False

def main():
    edge_lists = read_multiple_edge_list_formats(INPUT_PATH)
    graphs = [build_directed_graph_from_adjacency_list(g.num_vertices, g.adjacency_list) for g in edge_lists]
    soln = [is_acyclic(g) for g in graphs]
    write_solution(soln)

if __name__ == '__main__':
    main()