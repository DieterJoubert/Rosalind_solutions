def other(x):
  fin = open(x)
  fout = open('out.txt', 'w')
  count = 0
  for line in fin:
    if count % 2 == 1:
      fout.write(line)
    count += 1
  fin.close()
  fout.close()

