def sseq():
  fin = open("rosalind_sseq.txt")
  DNA = ""
  motif = ""

  stringcount = 0
  for line in fin:
    line = line.replace('\n', '')
    if line[0] == '>':
      stringcount += 1
      continue
    else:
      if stringcount == 1:
        DNA += line
      else:
        motif += line
  fin.close()

  results = []
  index = 0
  length = len(DNA)
  while(len(motif) > 0):
    term = motif[0]
    for i in range(index,length):
      if DNA[i] == term:
        results.append(i+1)
        index = i+1
        motif = motif[1:]
        break

  fout = open("out.txt","w")
  for i in results:
    fout.write(str(i) + " ")
  fout.close()
  



