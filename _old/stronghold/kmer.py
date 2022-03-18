def kmer():
  fin = open("rosalind_kmer.txt")
  data = ""

  for line in fin:
    line = line.replace('\n', '')
    if line[0:1] != '>':
      data += line
  fin.close()

  alphabet = ['A', 'C', 'G', 'T']
  lex = perms(alphabet,4,"",[])

  countlist = []
  for kmer in lex:
    count = 0
    for i in range(len(data)-3):
      if data[i:i+4] == kmer:
        count += 1
    countlist.append(count)

  string = " ".join(map(str,countlist))

  fout = open("out.txt","w")
  fout.write(string)
  fout.close()

def perms(alphabet, n, acc, res):
  if n==0:
    res.append(acc)
  else:
    for c in alphabet:
      perms(alphabet, n-1, acc+c,res)
  return res






