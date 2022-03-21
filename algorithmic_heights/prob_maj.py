INPUT_PATH = './input/rosalind_maj.txt'
OUTPUT_PATH = './output/prob_maj.txt'

def write_solution(majority_elements):
    f = open(OUTPUT_PATH, "w")
    f.write(" ".join(map(str, majority_elements)))
    f.close()    

def get_data() -> int:
    with open(INPUT_PATH) as f:
        lines = f.read().splitlines()
        return [list(map(int, line.split()))  for line in lines[1:]]

def get_majority_element(nums):
    counts = {}
    threshold = len(nums) / 2

    for num in nums:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
            if counts[num] > threshold:
                return num
    
    return (-1)

def main():
    data = get_data()
    majority_elements = list(map(get_majority_element, data))
    write_solution(majority_elements)

if __name__ == '__main__':
    main()