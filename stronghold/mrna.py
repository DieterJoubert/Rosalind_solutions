def mrna():
  fin = open("rnatable.txt")
  rna = {}

  keycheck = True
  for line in fin:
    line = line.replace('\n', '')
    for word in line.split():
      if keycheck:
        last = word
      else:
        rna[last] = word
      keycheck = not keycheck  
  fin.close()

  protSources = {}
  for key, value in rna.items():
    if value in protSources:
      protSources[value] += 1
    else:
      protSources[value] = 1

  for key, value in protSources.items():
    print str(key) + " " + str(value)

  with open ("rosalind_mrna.txt", "r") as myfile:
    data = myfile.read().replace('\n', '')

  choices = []
  for i in data:
    choices.append(protSources[i])

  total = 1
  for term in choices:
    total = total * term

  total = total * protSources['Stop']

  return int(total % 1000000)
    

