INPUT_PATH = './input/rosalind_par3.txt'
OUTPUT_PATH = './output/prob_par3.txt'

def get_data() -> int:
    with open(INPUT_PATH) as f:
        lines = f.read().splitlines()
        return int(lines[0]), list(map(int, lines[1].split())) 

def write_solution(array):
    f = open(OUTPUT_PATH, "w")
    f.write(" ".join(map(str, array)))
    f.close()

def get_three_way_partitioned_array(n, array):
    pivot = array[0]
    low = []
    middle = [pivot]
    high = []

    for num in array[1:]:
        if num < pivot:
            low.append(num)
        elif num > pivot:
            high.append(num)
        else:
            middle.append(num)

    return low + middle + high


def main():
    n, A = get_data()
    partitioned_array = get_three_way_partitioned_array(n, A)
    write_solution(partitioned_array)

if __name__ == '__main__':
    main()