def ms():
  with open("rosalind_ms.txt") as myfile:
    head = [next(myfile) for x in xrange(2)]
  
  nums = head[1].replace('\n', '').split()
  nums = map(int,nums)

  result = mergesort(nums)

  fout = open('out.txt','w')
  fout.write(" ".join(map(str, result)))
  fout.close()

def mergesort(m):
  if len(m) <= 1:
    return m
  else:
    middle = len(m) / 2
    left = m[0:middle]
    right = m[middle:]
    left = mergesort(left)
    right = mergesort(right)
    result = merge(left, right)
    return result

def merge(left,right):
  result = []
  while (len(left) > 0 and len(right) > 0):
    if left[0] <= right[0]:
      result.append(left[0])
      left = left[1:]
    else:
      result.append(right[0])
      right = right[1:]
  if len(left) > 0:
    result += left
  if len(right) > 0:
    result += right
  return result



