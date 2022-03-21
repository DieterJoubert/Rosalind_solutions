from utils import get_fasta_data

DATA_PATH = './data/rosalind_gc.txt'
OUTPUT_PATH = './output/prob_gc.txt'

def get_gc_content(dna: str) -> float:
    count = 0
    for c in dna:
        if c == 'C' or c == 'G':
            count += 1
    return count / len(dna)

def get_id_to_gc_content(data):
    contents = {}
    for (id, dna) in data.items():
        contents[id] = get_gc_content(dna)
    return contents

def get_id_of_max(data):
    return max(data, key=data.get)

def write_solution(id: str, gc_content: float):
    f = open(OUTPUT_PATH, "w")
    gc_percent = gc_content * 100
    f.writelines([id, '\n', str(gc_percent)])
    f.close()

def main():
    data = get_fasta_data(DATA_PATH)
    id_to_gc_content = get_id_to_gc_content(data)
    soln_id = get_id_of_max(id_to_gc_content)
    write_solution(soln_id, id_to_gc_content[soln_id])

if __name__ == '__main__':
    main()