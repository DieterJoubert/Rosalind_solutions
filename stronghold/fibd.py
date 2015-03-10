def fibd(n,m):
  rabbits = []
  rabbits.append(1)
  for i in range(m):
    rabbits.append(0)

  term = 0
  while term < n:
    born = 0
    for i in range(1,len(rabbits)-1):
      born += rabbits[i]
    rabbits.insert(0,born)
    rabbits = rabbits[:-1]
    term += 1

  grown = 0
  for i in range(1,len(rabbits)):
    grown += rabbits[i]
  return grown
