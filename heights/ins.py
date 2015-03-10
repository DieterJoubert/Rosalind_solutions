def ins():
  with open("ins.txt") as myfile:
    head = [next(myfile) for x in xrange(2)]

  n = int(head[0].replace('\n', ''))
  strArr = head[1].replace('\n', '')

  array = []
  for word in strArr.split():
    array.append(int(word))

  count = 0
  for i in range(1,n):
    k = i
    while k > 0 and array[k] < array[k-1]:
      temp = array[k-1]
      array[k-1] = array[k]
      array[k] = temp
      k -= 1
      count += 1

  print count

