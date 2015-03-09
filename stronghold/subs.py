def subs():
  with open("subs.txt") as myfile:
    head = [next(myfile) for x in xrange(2)]

  data = head[0].replace('\n', '')
  motif = head[1].replace('\n', '')
  myfile.close()

  k = len(motif)
  found = []
  for i in range(len(data)):
    if data[i:i+k] == motif:
      found.append(i+1)

  string = ""
  for f in found:
    string += str(f) + " "
  string = string[:-1]

  print string


