FILE = "./data/rosalind_bfs.txt"
OUTPUT = "out.txt"

def main():
	lines = open(FILE).read().splitlines()
	graph = parse_directed_graph(lines)
	result = bfs_list(graph)

	out = open(OUTPUT, "w")
	out.write(" ".join(map(str, result)))
	out.close()

def parse_directed_graph(lines):
	meta_line = lines[0]
	data_lines = lines[1:]
	n, m = map(int, meta_line.split())

	graph = {i: [] for i in range(1,n+1)}
	for line in data_lines:
		a, b = map(lambda x: int(x), line.split())
		graph[a].append(b)
	return graph

def bfs_list(graph):
	shortest_paths = []

	for k in sorted(graph.keys()):
		shortest_paths.append(bfs(graph, k))
	return shortest_paths

# BFS from 1 to other nodes
def bfs(graph, target):
	q = [(1, 0)]
	visited = [1]

	while q:
		curr, dist = q[0]		
		q = q[1:]

		if curr == target:
			return dist

		visited.append(curr)

		for neigh in graph[curr]:
			if neigh not in visited:
				q.append((neigh, dist+1))

	return (-1)

if __name__ == "__main__":
	main()