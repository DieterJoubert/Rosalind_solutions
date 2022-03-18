def mer():
  with open("rosalind_mer.txt") as myfile:
    head = [next(myfile) for x in xrange(4)]
  myfile.close()

  strA = head[1].replace('\n', '')  
  A = []
  for word in strA.split():
    A.append(int(word))

  strB = head[3].replace('\n', '')  
  B = []
  for word in strB.split():
    B.append(int(word))

  acc = []

  while len(A) > 0 or len(B) > 0:
    if not A:
      acc += B
      break
    if not B:
      acc += A
      break

    if A[0] < B[0]:
      acc += [ A[0] ]
      A.pop(0)
    elif A[0] >= B[0]:
      acc += [ B[0] ]
      B.pop(0)

  fout = open('out.txt','w')
  for i in acc:
    fout.write(str(i) + " ")
  fout.close()
