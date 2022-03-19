DATA_SRC = './data/rosalind_lgis.txt'
OUTPUT_SRC = './output/prob_lgis.txt'

def get_data():
    with open(DATA_SRC) as f:
        lines = f.read().splitlines()
        return [int(lines[0]), list(map(lambda x: int(x), lines[1].split()))]

def get_best_and_backtrack(array, increasing=True):
    fn = (lambda p1, p2: p1 > p2) if increasing==True else (lambda p1, p2: p1 < p2)

    best = [1] * len(array)
    backtrack = [None] * len(array)

    for i in range(1, len(array)):
        for j in range(0, i):
            if fn(array[i], array[j]) and best[j] + 1 > best[i]:
                best[i] = best[j] + 1
                backtrack[i] = j

    return best, backtrack

def get_longest_subsequence(perm, best, backtrack):
    curr_idx = best.index(max(best))
    
    subsequence = []

    while True:
        subsequence.insert(0, perm[curr_idx])
        curr_idx = backtrack[curr_idx]
        if curr_idx == None:
            break

    return subsequence

def get_longest_increasing(perm):
    best, backtrack = get_best_and_backtrack(perm)
    lis = get_longest_subsequence(perm, best, backtrack)
    return lis

def get_longest_decreasing(perm):
    best, backtrack = get_best_and_backtrack(perm, increasing=False)
    lds = get_longest_subsequence(perm, best, backtrack)
    return lds

def write_solution(lis, lds):
    f = open(OUTPUT_SRC, "w")
    f.write(" ".join(map(lambda x: str(x), lis)) + "\n")
    f.write(" ".join(map(lambda x: str(x), lds)) + "\n")
    f.close()

def main():
    _, perm = get_data()
    lis = get_longest_increasing(perm)
    lds = get_longest_decreasing(perm)
    write_solution(lis, lds)

if __name__ == '__main__':
    main()