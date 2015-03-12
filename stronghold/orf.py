def orf():
  fin = open("rosalind_orf.txt")
  DNA = ""
  for line in fin:
    line = line.replace('\n', '')
    if line[0:1] == '>':
      continue
    else:
      DNA += line

  RNA = DNA.replace('T','U')
  results = transcript(RNA)

  rev = reverse_compliment_RNA(RNA)
  revresults = transcript(rev)
  for r in revresults:
    if r not in results:
      results.append(r)

  fout = open('out.txt', 'w')
  for r in results:
    fout.write(r + '\n')
  fout.close()

def reverse_compliment_RNA(data):
  revcomp = ""
  switch = {
    'A': 'U',
    'U': 'A',
    'G': 'C',
    'C': 'G'
  }
  length = len(data)
  for i in range(0,length):
    revcomp += switch[data[length-1-i]]
  return revcomp

def transcript(RNA):
  convert = read_RNA_table()
  startPositions = []

  for i in range(0,len(RNA)):
    if RNA[i:i+3] == "AUG":
      startPositions.append(i)

  results = []

  for s in startPositions:
    protein = ""
    for i in range(s,len(RNA),3):

      segment = RNA[i:i+3]
      try:
        prot = convert[segment]
      except Exception, e:
        break

      if prot == "Stop":
        results.append(protein)
        break
      else:
        protein += prot

  return results

def read_RNA_table():
  fin = open("rnatable.txt")
  convert = {}

  keycheck = True
  for line in fin:
    line = line.replace('\n', '')
    for word in line.split():
      if keycheck:
        last = word
      else:
        convert[last] = word
      keycheck = not keycheck  
  fin.close()

  return convert