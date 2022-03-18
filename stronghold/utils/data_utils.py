from typing import List

def get_dna_data(src: str) -> str:
    with open(src) as f:
        lines = f.read().splitlines()
        return lines[0]

def write_solution(destination: str, content: List[str]):
    f = open(destination, "w")
    for c in content:
        f.write(c)
    f.close()
