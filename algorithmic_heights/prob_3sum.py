INPUT_PATH = './input/rosalind_3sum.txt'
OUTPUT_PATH = './output/prob_3sum.txt'

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

def get_three_sum_indices(nums):
    num_to_idx = {}

    for idx in range(len(nums)):
        num = nums[idx]
        if num not in num_to_idx:
            num_to_idx[num] = {idx}
        else:
            num_to_idx[num].add(idx)

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            num_i, num_j = nums[i], nums[j]
            remainder = -(num_i + num_j)

            if remainder in num_to_idx:
                leftover_indices = num_to_idx[remainder] - {num_i, num_j}
                if leftover_indices:
                    return tuple(sorted([i, j, list(leftover_indices)[0]]))

    return (-1)

def main():
    data = get_data()
    all_three_sum_indices = list(map(get_three_sum_indices, data))
    print(all_three_sum_indices)
    write_solution(all_three_sum_indices)

if __name__ == '__main__':
    main()