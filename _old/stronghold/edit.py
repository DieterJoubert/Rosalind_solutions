def edit():
  fin = open("rosalind_edit.txt")
  s1 = ""
  s2 = ""

  stringcount = 0
  for line in fin:
    line = line.replace('\n', '')
    if line[0] == '>':
      stringcount += 1
    else:
      if stringcount == 1:
        s2 += line
      else:
        s1 += line
  fin.close()

  matrix = [[0 for x in range(len(s1)+1)] for y in range(len(s2)+1)]

  for i in range(1,len(s1)+1):
    matrix[0][i] = i

  for j in range(1,len(s2)+1):
    matrix[j][0] = j

  for i in range(len(s2)):
    for j in range(len(s1)):
      x=i+1
      y=j+1
      if s1[j] == s2[i]:
        matrix[x][y] = matrix[x-1][y-1]
      else:
        matrix[x][y] = min(matrix[x-1][y]+1,matrix[x][y-1]+1,matrix[x-1][y-1]+1)

  x = len(s2)
  y = len(s1)

  """
  for i in range(len(s2)+1):
    print matrix[i]
  """

  print matrix[x][y]