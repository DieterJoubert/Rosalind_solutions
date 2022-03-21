from typing import List

def get_data() -> List[int]:
    with open('./input/rosalind_fib.txt') as f:
        lines = f.read().splitlines()
        return map(lambda x: int(x), lines[0].split())

def get_final_population(sequence: List[int], n: int, k: int):
    while len(sequence) < n:
        next_pop = sequence[-2] * k + sequence[-1]
        sequence.append(next_pop)
    return sequence[-1]

def main():
    n, k = get_data()
    sequence = [1, 1]
    soln = get_final_population(sequence, n, k)
    print(soln)

if __name__ == '__main__':
    main()