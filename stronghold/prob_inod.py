DATA_PATH = './data/rosalind_inod.txt'

def get_data():
    with open(DATA_PATH) as f:
        lines = f.read().splitlines()
        return int(lines[0])

def main():
    n = get_data()
    soln = n-2
    print(str(soln))

if __name__ == '__main__':
    main()