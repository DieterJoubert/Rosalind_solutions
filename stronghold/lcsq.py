def backtrack(matrix,s1,s2,x,y):
  print "once"
  if y == 0 or x == 0:
    return ""
  elif s1[y-1] == s2[x-1]:
    return backtrack(matrix, s1, s2, x-1, y-1) + s1[y-1]
  else:
    if matrix[x][y-1] > matrix[x-1][y]:
      return backtrack(matrix, s1, s2, x, y-1)
    else:
      return backtrack(matrix, s1, s2, x-1, y)

def lcsq():
  fin = open("rosalind_lcsq.txt")
  s1 = ""
  s2 = ""

  stringcount = 0
  for line in fin:
    line = line.replace('\n', '')
    if line[0] == '>':
      stringcount += 1
      continue
    else:
      if stringcount == 1:
        s2 += line
      else:
        s1 += line
  fin.close()

  print s1
  print s2

  matrix = [[0 for x in range(len(s1)+1)] for y in range(len(s2)+1)]

  for i in range(len(s2)):
    for j in range(len(s1)):
      x=i+1
      y=j+1
      if s1[j] == s2[i]:
        matrix[x][y] = matrix[x-1][y-1] + 1
      else:
        matrix[x][y] = max(matrix[x-1][y],matrix[x][y-1])

  longest = ""

  x = len(s2)
  y = len(s1)

  while (True):
    if y == 0 or x == 0:
      break
    elif s1[y-1] == s2[x-1]:
      longest = s1[y-1] + longest      
      x = x-1 
      y = y-1
    else:
      if matrix[x][y-1] > matrix[x-1][y]:
        y = y-1
      else:
        x = x-1

  fout = open("out.txt","w")
  fout.write( longest )
  fout.close()


























