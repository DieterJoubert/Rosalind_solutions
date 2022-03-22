INPUT_PATH = './input/rosalind_par.txt'
OUTPUT_PATH = './output/prob_par.txt'

def get_data() -> int:
    with open(INPUT_PATH) as f:
        lines = f.read().splitlines()
        return int(lines[0]), list(map(int, lines[1].split())) 

def write_solution(array):
    f = open(OUTPUT_PATH, "w")
    f.write(" ".join(map(str, array)))
    f.close()

def get_two_way_partitioned_array(array):
    pivot = array[0]
    low = []
    high = []

    for num in array[1:]:
        if num < pivot:
            low.append(num)
        else:
            high.append(num)

    return low + [pivot] + high

def main():
    n, A = get_data()
    partitioned_array = get_two_way_partitioned_array(A)
    write_solution(partitioned_array)

if __name__ == '__main__':
    main()