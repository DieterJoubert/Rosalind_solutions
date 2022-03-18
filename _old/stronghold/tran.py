def tran():
  strOne = ""
  strTwo = ""

  transitions = [['A', 'G'], ['C', 'T']]
  transversions = [['A', 'C'], ['G', 'T']]

  fin = open("rosalind_tran.txt")

  stringcount = 0
  for line in fin:
    line = line.replace('\n', '')
    if line[0] == '>':
      stringcount += 1
      continue
    else:
      if stringcount == 1:
        strOne += line
      else:
        strTwo += line
  fin.close()
  
  transitionCount = 0
  transversionCount = 0

  for i in range(len(strOne)):
    if strOne[i] != strTwo[i]:
      bases = sorted( [strOne[i],strTwo[i]] )
      if bases in transitions:
        transitionCount += 1
      else:
        transversionCount += 1

  print float(transitionCount) / float(transversionCount)
