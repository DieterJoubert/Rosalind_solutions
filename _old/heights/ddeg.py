FILE = "./data/rosalind_ddeg.txt"

def main():
	lines = open(FILE).read().splitlines()
	meta_line = lines[0]
	data_lines = lines[1:]

	num_nodes, num_edges = map(int, meta_line.split())
	graph = parse_graph(data_lines, num_nodes)
	
	result = ddeg(graph)

	out = open("out.txt", "w")
	out.write(" ".join(map(str, result)))
	out.close()

def parse_graph(lines, n):
	graph = {i: [] for i in range(1,n+1)}
	for line in lines:
		a, b = map(lambda x: int(x), line.split())
		graph[a].append(b)
		graph[b].append(a)
	return graph

def degree_list(graph):
	degrees = []

	for i in sorted(graph.keys()):
		degrees.append(len(graph[i]))

	return degrees

def ddeg(graph):
	degrees = degree_list(graph)
	neighbor_sum_degrees = []

	for i in sorted(graph.keys()):
		neighbor_sum = 0
		for neighbor in graph[i]:
			neighbor_sum += degrees[neighbor-1]
		neighbor_sum_degrees.append(neighbor_sum)

	return neighbor_sum_degrees

if __name__ == "__main__":
	main()