INPUT_PATH = './input/rosalind_sset.txt'

def get_data():
    with open(INPUT_PATH) as f:
        lines = f.read().splitlines()
        return int(lines[0])

def main():
    n = get_data()
    soln = (2 ** n) % 1000000
    print(str(soln))

if __name__ == '__main__':
    main()