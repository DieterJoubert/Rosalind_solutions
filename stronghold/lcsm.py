def lcsm():
  fin = open("rosalind_lcsm.txt")
  strings = []

  reading = False
  nextStr = ""
  for line in fin:
    line = line.replace('\n', '')
    if line[0] == '>':
      reading = True
      if nextStr != "":
        strings.append(nextStr)
        nextStr = ""
      continue
    else:
      nextStr += line
  strings.append(nextStr)
  fin.close()

  shortest = strings[0]
  for s in strings:
    if len(s) < len(shortest):
      shortest = s

  strings = [y for y in strings if y != shortest]

  best = ""
  length = len(shortest)
  for size in range(1,length+1):
    bestNow = best
    for i in range(0,length):
      term = shortest[i:i+size]
      if len(term) < len(best):
        break
      if check(term,strings) == True:
        best = term
        break
    if bestNow == best:
      break

  fout = open("out.txt","w")
  fout.write(best)
  fout.close()

def check(term,strings):
  size = len(term)
  for s in strings:
    length = len(s)
    for i in range(0,length):
      if s[i:i+size] == term:
        break
      if i==length-1:
        return False
  return True




