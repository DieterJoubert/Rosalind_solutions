INPUT_PATH = './input/rosalind_seto.txt'
OUTPUT_PATH = './output/prob_seto.txt'

def get_data():
    with open(INPUT_PATH) as f:
        lines = f.read().splitlines()
        return int(lines[0]), eval(lines[1]), eval(lines[2])

def write_solution(sets):
    f = open(OUTPUT_PATH, "w")
    for set in sets:
        f.write(str(set) + "\n")
    f.close()

def main():
    n, A, B = get_data()
    U = {x for x in range(1, n+1)}
    sets = [A.union(B), A.intersection(B), A - B, B - A, U - A, U - B]
    write_solution(sets)

if __name__ == '__main__':
    main()