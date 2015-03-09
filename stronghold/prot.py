def prot():

  #load the RNA table
  fin = open("rnatable.txt")
  rna = {}

  keycheck = True
  for line in fin:
    line = line.replace('\n', '')
    for word in line.split():
      if keycheck:
        last = word
        keycheck = not keycheck
      else:
        rna[last] = word
        keycheck = not keycheck
  fin.close()

  #now load and translate the RNA string
  with open ("prot.txt", "r") as myfile:
    data = myfile.read().replace('\n', '')

  protStr = ""
  for i in range(0,len(data),3):
    protein = rna[ data[i:i+3] ]
    if protein == "Stop":
      break
    protStr += protein

  fout = open("out.txt","w")
  fout.write(protStr)
  fout.close()
