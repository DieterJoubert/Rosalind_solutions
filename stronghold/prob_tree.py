from tkinter import X
from typing import List
from collections import deque

DATA_SRC = './data/rosalind_tree.txt'

def get_data():
    with open(DATA_SRC) as f:
        lines = f.read().splitlines()
        n = int(lines[0])
        adjacency_list = []
        for adj_line in lines[1:]:
            adjacency_list.append(tuple(map(lambda x: int(x), adj_line.split())))
    return n, adjacency_list

def get_tree(n, adjacency_list):
    tree = {x: [] for x in range(1, n+1)}

    for (x, y) in adjacency_list:
        tree[x].append(y)
        tree[y].append(x)

    return tree

def get_connected_component_coloring(n, tree):
    coloring = {x: None for x in range(1, n+1)}
    curr_color = 1

    for x in range(1, n+1):
        if coloring[x]:
            continue

        q = deque()
        q.append(x)

        while q:
            curr_node = q.popleft()
            if coloring[curr_node]:
                continue

            coloring[curr_node] = curr_color

            for neighbor in tree[curr_node]:
                q.append(neighbor)

        curr_color += 1

    return coloring

def main():
    n, adjacency_list = get_data()
    tree = get_tree(n, adjacency_list)
    connect_component_coloring = get_connected_component_coloring(n, tree)
    print(max(connect_component_coloring.values()) - 1)

if __name__ == '__main__':
    main()