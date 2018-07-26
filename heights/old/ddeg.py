import Queue

def ddeg():
  fin = open("rosalind_ddeg.txt")
  first_read = False

  graph = {}
  first = True

  for line in fin:
    if first: 
      first = False
      num_nodes = int(line.split()[0])
      for i in range(1,num_nodes+1):
        graph[i] = []
    else:
      line = line.replace('\n', '')
      x = int(line.split()[0])
      y = int(line.split()[1])
      graph[x] = graph[x] + [y]
      graph[y] = graph[y] + [x]

  fin.close()

  neighbor_count = []


  for node, neighbors in graph.items():
    print neighbors
    neighbor_sum = 0
    for n in neighbors:
      neighbor_sum += len(graph[n])
    neighbor_count.insert( node-1, neighbor_sum )

  print neighbor_count


  fout = open("out.txt","w")
  fout.write(" ".join(map(str, neighbor_count)))
  fout.close()

if __name__ == '__main__':
  ddeg()