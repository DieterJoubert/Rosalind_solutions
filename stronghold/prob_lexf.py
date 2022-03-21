DATA_PATH = './data/rosalind_lexf.txt'
OUTPUT_PATH = './output/prob_lexf.txt'

def get_data():
    with open(DATA_PATH) as f:
        lines = f.read().splitlines()
        return lines[0].split(), int(lines[1])

def get_permutations(symbols, n):
    perms = [x for x in symbols]

    while len(perms[0]) < n:
        next_iter = []
        for perm in perms:
            for s in symbols:
                next_iter.append(perm + s)
        perms = next_iter

    return sorted(perms)

def write_solution(perms):
    f = open(OUTPUT_PATH, "w")
    for perm in perms:
        f.write(perm + "\n")
    f.close()

def main():
    symbols, n = get_data()
    perms = get_permutations(symbols, n)
    write_solution(perms)

if __name__ == '__main__':
    main()