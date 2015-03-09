def fib(n,k):
  offspring = 1
  grown = 0
  term = 0
  while term < n:
    new = grown * k
    grown += offspring
    offspring = new
    term += 1
  return grown
