INPUT_PATH = './input/rosalind_2sum.txt'
OUTPUT_PATH = './output/prob_2sum.txt'

def get_data() -> int:
    with open(INPUT_PATH) as f:
        lines = f.read().splitlines()
        return [list(map(int, line.split()))  for line in lines[1:]]

def write_solution(all_two_sum_indices):
    f = open(OUTPUT_PATH, "w")
    for el in all_two_sum_indices:
        if isinstance(el, int):
            f.write(str(el) + "\n")
        else:
            f.write(" ".join(map(lambda x: str(x+1), el)) + "\n")
    f.close()

def get_two_sum_indices(nums):
    num_to_idx = {}

    for idx in range(len(nums)):
        neg = -nums[idx]
        if neg in num_to_idx:
            return (num_to_idx[neg], idx)
        else:
            num_to_idx[nums[idx]] = idx

    return (-1)

def main():
    data = get_data()
    all_two_sum_indices = list(map(get_two_sum_indices, data))
    write_solution(all_two_sum_indices)

if __name__ == '__main__':
    main()