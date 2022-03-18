def splc():
  fin = open("rosalind_splc.txt")
  DNA = None
  introns = []

  readingDNA = False
  for line in fin:
    line = line.replace('\n', '')
    if line[0:1] == '>':
      readingDNA = False
      continue
    else:
      if readingDNA == True:
        DNA += line
      elif not DNA:
        DNA = line
        readingDNA = True
      else:
        introns.append(line)
  fin.close()

  """
  print DNA
  for i in introns:
    print i
  """

  for intron in introns:
      DNA = DNA.replace(intron, '')

  RNA = DNA.replace('T','U')

  print rna_to_protein(RNA)


def rna_to_protein(rna):
  #load the RNA table
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

  protStr = ""
  for i in range(0,len(rna),3):
    protein = convert[ rna[i:i+3] ]
    if protein == "Stop":
      break
    protStr += protein

  return protStr
