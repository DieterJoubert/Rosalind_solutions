def sumOdd(x,y):
  sum = 0
  while x <= y:
    if x % 2 == 1:
      sum += x
    x += 1
  return sum
