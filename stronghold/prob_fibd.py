from typing import List

DATA_SRC = './data/rosalind_fibd.txt'

def get_data() -> List[int]:
    with open(DATA_SRC) as f:
        lines = f.read().splitlines()
        return map(lambda x: int(x), lines[0].split())

def get_final_population(n: int, m: int):
    pop = {
        0: 1
    }

    curr_month = 1

    while curr_month < n:
        newborns = sum([pop[age] for age in range(1, m) if age in pop])

        new_pop = {age+1: pop[age] for age in pop.keys() if age < m-1}
        new_pop[0] = newborns

        pop = new_pop
        curr_month += 1

    return sum(pop.values())

def main():
    n, m = get_data()
    soln = get_final_population(n, m)
    print(soln)

if __name__ == '__main__':
    main()