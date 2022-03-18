import Queue

def long():
  strings = {}

  fin = open("rosalind_long.txt")

  identifier = ""
  data = ""

  for line in fin:
    line = line.replace('\n', '')
    if line[0] == '>':
      if data != "":
        strings[data] = identifier
        identifier = ""
        data = ""
      identifier = line[1:]
    else:
      data += line
  fin.close()

  edge_queue = Queue.PriorityQueue()

  for start, start_ID in strings.items():
    for end, end_ID in strings.items():
      if start_ID != end_ID:
        max_match = 0
        i = -1
        j = 1        
        for x in range(min(len(start), len(end))):
          if start[i-x:] == end[:j+x]:
            max_match = x+1

        edge_queue.put( (-max_match, start, end) )

  strings_done = []

  # get first to start with
  (overlap, start, end) = edge_queue.get()
  overlap = abs(overlap)
  superstring = start[0:len(start)-overlap] + end
  strings.pop(start, 0)
  strings.pop(end, 0)

  leftmost = start
  rightmost = end

  while len(strings):
    (overlap, start, end) = edge_queue.get()
    overlap = abs(overlap)
    if (start not in edge_queue) and (end not in edge_queue):
      continue

    




        



if __name__ == '__main__':
  long()