INPUT_PATH = './input/rosalind_fibo.txt'

def get_data() -> int:
    with open(INPUT_PATH) as f:
        lines = f.read().splitlines()
        return int(lines[0])

def get_fibo_sequence(n):
    seq = [0, 1, 1]

    while len(seq) <= n:
        seq.append(seq[-1] + seq[-2])

    return seq

def main():
    n = get_data()
    fibo_sequence = get_fibo_sequence(n)
    print(fibo_sequence[-1])

if __name__ == '__main__':
    main()