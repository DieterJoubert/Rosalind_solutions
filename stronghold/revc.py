def revc():
  fout = open("out.txt","w")
  with open ("revc.txt", "r") as myfile:
    data = myfile.read().replace('\n', '')

  switch = {
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G'
  }

  length = len(data)
  for i in range(0,length):
    fout.write(switch[data[length-1-i]])

  myfile.close()
  fout.close()

