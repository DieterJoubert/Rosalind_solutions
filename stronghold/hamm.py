def hamm():
  strOne = ""
  strTwo = ""
  distance = 0

  with open("hamm.txt") as myfile:
    head = [next(myfile) for x in xrange(2)]
  
  strOne = head[0].replace('\n', '')
  strTwo = head[1].replace('\n', '')

  for i in range(0,len(strOne)):
    if strOne[i] != strTwo[i]:
      distance += 1

  myfile.close()
  print(distance)
