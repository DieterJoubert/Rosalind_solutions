INPUT_PATH = './input/rosalind_med.txt'

def get_data() -> int:
    with open(INPUT_PATH) as f:
        lines = f.read().splitlines()
        return int(lines[0]), list(map(int, lines[1].split())), int(lines[2])

def partition(array):
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

    return (low, middle, high)


def get_kth_smallest(array, k):
    curr_array = array
    curr_pointer = 0

    while True:
        low, middle, high = partition(curr_array)
        if curr_pointer + len(low) > k:
            curr_array = low
        elif curr_pointer + len(low) + len(middle) < k:
            curr_array = high
            curr_pointer += len(low) + len(middle)
        else:
            return middle[0]

def main():
    n, A, k = get_data()
    kth_smallest = get_kth_smallest(A, k)
    print(kth_smallest)

if __name__ == '__main__':
    main()