def cons():
  fin = open("rosalind_cons.txt")
  data = []

  #TODO: clean up reading in DNA strings
  dna = []
  for line in fin:
    line = line.replace('\n', '')
    if line[0:1] == '>':
      if dna != []: 
        data.append(dna)
      dna = []   
    else:
      for c in list(line):
        dna.append(c)
  if dna != []: 
    data.append(dna)

  fin.close()

  """
  for i in range(len(data)):
    string =""
    for j in range(len(data[i])):
      string += str(data[i][j])
    print string
  """

  profile = {'A': [], 'C': [], 'G': [], 'T': []}
  for key in profile:
    for i in range(len(data[0])):
      profile[key].append(0)

  for i in range(len(data)):
    for j in range(len(data[i])):
      profile[ data[i][j] ][j] += 1

  dominant = ""
  for i in range(len(data[0])):
    letter = 'A'
    count = 0
    for key in profile:
      if profile[key][i] > count:
        count = profile[key][i]
        letter = key
    dominant += letter

  fout = open("out.txt","w")
  fout.write(dominant + '\n')

  fout.write( "A: " + ' '.join(map(str,profile['A'])) + '\n')
  fout.write( "C: " + ' '.join(map(str,profile['C'])) + '\n')
  fout.write( "G: " + ' '.join(map(str,profile['G'])) + '\n')
  fout.write( "T: " + ' '.join(map(str,profile['T'])) )


  """
  for key in sorted(profile):
    string = key + ": "
    for j in range(len(profile[key])):
      string += str(profile[key][j]) + " "
    fout.write(string[:-1] + '\n')
  """

  fout.close()