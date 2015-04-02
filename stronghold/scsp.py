
"""
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
"""

def scsp():
  with open("rosalind_scsp.txt") as myfile:
    head = [next(myfile) for x in xrange(2)]

  s1 = head[0].replace('\n', '')
  s2 = head[1].replace('\n', '')

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
    if y == 0:
      longest = s2[0:x] + longest
      break
    elif x == 0:
      longest = s1[0:y] + longest
      break
    elif s1[y-1] == s2[x-1]:
      longest = s1[y-1] + longest      
      x = x-1 
      y = y-1
    else:
      if matrix[x][y-1] > matrix[x-1][y]:
        longest = s1[y-1] + longest
        y = y-1
      else:
        longest = s2[x-1] + longest
        x = x-1

  fout = open("out.txt","w")
  fout.write( longest )
  fout.close()
