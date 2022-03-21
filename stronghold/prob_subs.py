from typing import List

INPUT_PATH = './input/rosalind_subs.txt'
OUTPUT_PATH = "./output/prob_subs.txt"

def get_data() -> List[str]:
    with open(INPUT_PATH) as f:
        lines = f.read().splitlines()
        return lines

def find_substring_indices(s: str, t: str):
    positions = []

    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            positions.append(i)

    return positions

def write_solution(positions):
    f = open(OUTPUT_PATH, "w")
    f.write(" ".join(map(lambda x: str(x + 1), positions)))
    f.close()

def main():
    s, t = get_data()
    positions = find_substring_indices(s, t)
    write_solution(positions)

if __name__ == '__main__':
    main()