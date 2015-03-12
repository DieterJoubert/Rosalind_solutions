def prtm():
  #read monoisotopic mass table to get weights of proteins
  fin = open("monomasstable.txt")
  masstable = {}

  keycheck = True
  for line in fin:
    line = line.replace('\n', '')
    for word in line.split():
      if keycheck:
        last = word
      else:
        masstable[last] = word
      keycheck = not keycheck  
  fin.close()

  with open ("rosalind_prtm.txt", "r") as myfile:
    data = myfile.read().replace('\n', '')

  totalweight = float(0)
  for p in data:
    totalweight += float(masstable[p])

  return float(totalweight)