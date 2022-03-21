INPUT_PATH = './input/rosalind_nwck.txt'
OUTPUT_PATH = './output/prob_nwck.txt'

#https://github.com/jarecot/Rosalind/blob/master/scripts/Newick_Trees.py

#TODO

def get_data():
    with open(INPUT_PATH) as f:
        lines = [x for x in f.read().splitlines() if x]
        return lines

def get_tree_from_newick(newick_rep):
    edges = set()
    nodes = {}

    newick_rep = newick_rep.replace(',', ' ').replace('(','( ').replace(')',' )').strip(';')
    newick_list = newick_rep.split()
    print(newick_rep)
    print(newick_list)

def main():
    lines = get_data()
    tree = get_tree_from_newick(lines[0])
    #print(lines)

if __name__ == '__main__':
    main()