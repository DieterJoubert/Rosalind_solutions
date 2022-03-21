INPUT_PATH = './input/rosalind_trie.txt'
OUTPUT_PATH = './output/prob_trie.txt'

class Trie:
    def __init__(self):
        self.nodes = {1: []}
        self.edges = {}
        self.max_node = 1

    def add_string(self, s):
        pointer = 1

        for c in s:
            neighbors = self.nodes[pointer]
            edge_label_to_neighbor = {self.edges[(pointer, n)]: n for n in neighbors}

            if c in edge_label_to_neighbor:
                pointer = edge_label_to_neighbor[c]
            else:
                self.max_node = self.max_node + 1
                self.nodes[pointer].append(self.max_node)
                self.nodes[self.max_node] = []
                self.edges[(pointer, self.max_node)] = c
                pointer = self.max_node
    
def get_data():
    with open(INPUT_PATH) as f:
        lines = f.read().splitlines()
        return lines

def write_solution(trie):
    f = open(OUTPUT_PATH, "w")
    for edge, label in trie.edges.items():
        f.write(f'{edge[0]} {edge[1]} {label} \n')
    f.close()

def build_trie(dna_strings):
    trie = Trie()

    for dna in dna_strings:
        trie.add_string(dna)

    return trie

def main():
    dna_strings = get_data()
    trie = build_trie(dna_strings)
    write_solution(trie)

if __name__ == '__main__':
    main()