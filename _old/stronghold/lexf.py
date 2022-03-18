def lexf():
  with open("rosalind_lexf.txt") as myfile:
    head = [next(myfile) for x in xrange(2)]
  
  lex = head[0].replace('\n', '').split()
  length = int(head[1].replace('\n', ''))

  results = perms(lex,length,"",[])

  fout = open("out.txt","w")
  for i in results:
    fout.write(i + '\n')
  fout.close()

def perms(alphabet, n, acc, res):
  if n==0:
    res.append(acc)
  else:
    for c in alphabet:
      perms(alphabet, n-1, acc+c,res)
  return res