def revp():
  fin = open("rosalind_revp.txt")
  DNA = ""
  for line in fin:
    line = line.replace('\n', '')
    if line[0] == '>':
      continue
    else:
      DNA += line
  fin.close()

  results = []

  bound = len(DNA)
  for index in range(bound):
    for seglen in range(4,13):
      if index+seglen > bound:
        continue

      seg = DNA[index:index+seglen]

      if seg == reverse_compliment_DNA(seg):
        position = index+1
        results.append((position,seglen))

  fout = open('out.txt', 'w')
  for pos, length in results:
    fout.write(str(pos) + " " + str(length) + '\n')
  fout.close() 

def reverse_compliment_DNA(data):
  revcomp = ""
  switch = {
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G'
  }
  length = len(data)
  for i in range(0,length):
    revcomp += switch[data[length-1-i]]

  return revcomp