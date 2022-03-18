def lexv():
  with open("rosalind_lexv.txt") as myfile:
    head = [next(myfile) for x in xrange(2)]
  
  lex = head[0].replace('\n', '').split()
  length = int(head[1].replace('\n', ''))


  results = perms(lex,length,"",[])

  fout = open("out.txt","w")
  for i in results:
    fout.write(i + '\n')
  fout.close()

def perms(alphabet, n, acc, res):
  if n > 0:
    for char in alphabet:
      res.append(acc + char)      
      res = perms(alphabet, n-1, acc+char,res)
  return res


