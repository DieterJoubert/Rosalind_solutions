INPUT_PATH = './input/rosalind_qs.txt'
OUTPUT_PATH = './output/prob_qs.txt'

def get_data() -> int:
    with open(INPUT_PATH) as f:
        lines = f.read().splitlines()
        return int(lines[0]), list(map(int, lines[1].split())) 

def write_solution(array):
    f = open(OUTPUT_PATH, "w")
    f.write(" ".join(map(str, array)))
    f.close()

def quicksort(array):
    if len(array) < 2:
        return array

    pivot = array[0]
    low = []
    middle = []
    high = []

    for num in array:
        if num < pivot:
            low.append(num)
        elif num > pivot:
            high.append(num)
        else:
            middle.append(num)

    return quicksort(low) + middle + quicksort(high)

def main():
    n, A = get_data()
    sorted_array = quicksort(A)
    print(sorted_array)
    write_solution(sorted_array)

if __name__ == '__main__':
    main()