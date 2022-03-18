def rna():
  fout = open("out.txt","w")
  with open ("rna.txt", "r") as myfile:
    data = myfile.read().replace('\n', '')
    
  for i in range(0,len(data)):
    if data[i] == 'T':
      fout.write('U')
    else:
      fout.write(data[i])

  myfile.close()
  fout.close()

