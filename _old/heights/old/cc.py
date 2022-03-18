import Queue

def cc():
  fin = open("rosalind_cc.txt")
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

  graph_coloring = {}
  for i in range(1, num_nodes+1):
    graph_coloring[i] = 0

  color = 1
  to_visit = Queue.Queue()


  for node, neighbors in graph.items():

    if graph_coloring[node] == 0:
      graph_coloring[node] = color

      for i in neighbors:
        to_visit.put(i)

      while not to_visit.empty():
        check_node = to_visit.get()

        if graph_coloring[check_node] == 0:
          graph_coloring[check_node] = color

          for neigh in graph[check_node]:
            to_visit.put(neigh)      
      color += 1

  print (color-1)

if __name__ == '__main__':
  cc()  