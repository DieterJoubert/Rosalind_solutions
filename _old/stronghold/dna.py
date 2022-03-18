def dna():
  fin = open("dna.txt")
  fout = open('out.txt', 'w')
  dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
  string = ""
  
  for line in fin:
    string = line
    break

  for i in range(0,len(string)):
    c = string[i]
    if c=='\n':
      break
    dic[c] += 1

  fout.write(str(dic['A']) + " " + str(dic['C']) + " " + str(dic['G']) + " " + str(dic['T']))
  fin.close()
  fout.close()
