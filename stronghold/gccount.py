def gccount():
  fin = open("gc.txt")
  data = {}
  gccount = {}

  for line in fin:
    line = line.replace('\n', '')
    if line[0:1] == '>':
      line = line[1:]
      data[line] = ""
      gccount[line] = 0
      last = lin
    else:
      data[last] += line
  fin.close()

  for key, string in data.items():
    counter = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for i in range(len(string)):
      counter[string[i]] += 1
    part = counter['C'] + counter['G']
    total = counter['A'] + counter['C'] + counter['G'] + counter['T']
    gccount[key] = float(part) / float(total) * 100

  maxGC = float(0)
  maxID = ""
  for key, value in gccount.items():
    if value > maxGC:
      maxGC = value
      maxID = key

  print maxID
  print maxGC