import Queue

def deg():
  fin = open("rosalind_deg.txt")
  first_read = False

  graph = {}
  first = True

  for line in fin:
    if first: 
      first = False
      continue
    line = line.replace('\n', '')
    x = int(line.split()[0])
    y = int(line.split()[1])

    if x in graph:
      graph[x] = graph[x] + [y]
    else:
      graph[x] = [y]

    if y in graph:
      graph[y] = graph[y] + [x]
    else:
      graph[y] = [x]
  fin.close()

  neighbor_count = []

  for node, neighbors in graph.items():
    neighbor_count.insert( node-1, len(neighbors) )

  fout = open("out.txt","w")
  fout.write(" ".join(map(str, neighbor_count)))
  fout.close()

if __name__ == '__main__':
  deg()