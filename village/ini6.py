def count(x):
  fin = open(x)
  fout = open('out.txt', 'w')
  dic = {}
  for line in fin:
    for word in line.split():
      if word in dic:
        dic[word] += 1
      else:
        dic[word] = 1
  for key, value in dic.items():
    fout.write(key + " " + str(value) + "\n")
  fin.close()
  fout.close()

