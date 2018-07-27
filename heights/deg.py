FILE = "./data/rosalind_deg.txt"

def main():
	lines = open(FILE).read().splitlines()
	meta_line = lines[0]
	data_lines = lines[1:]
	graph = parse_graph(data_lines)

	result = degree_list(graph)

	out = open("out.txt", "w")
	out.write(" ".join(map(str, result)))
	out.close()

def parse_graph(lines):
	graph = {}
	for line in lines:
		a, b = map(lambda x: int(x), line.split())
		if a not in graph:
			graph[a] = [b]
		else:
			graph[a].append(b)
		if b not in graph:
			graph[b] = [a]
		else:
			graph[b].append(a)
	return graph

def degree_list(graph):
	degrees = []

	for i in sorted(graph.keys()):
		degrees.append(len(graph[i]))

	return degrees

if __name__ == "__main__":
	main()