def lgis():
  with open("rosalind_lgis.txt") as myfile:
    head = [next(myfile) for x in xrange(2)]

  n = int(head[0].replace('\n', ''))
  s2 = head[1].replace('\n', '').replace(' ','')

  incr = ""
  for i in range(1,n+1):
    incr += str(i)

  decr = ""
  for i in reversed(range(1,n+1)):
    decr += str(i)


