def iprb(k,m,n):
  k = float(k)
  m = float(m)
  n = float(n)
  pop = k+m+n

  #if selecting dominant first
  dom = k/pop

  #if selecting heterozygous first
  hetfirst = m/pop
  popnew = pop-1
  hetdom = hetfirst * (k/popnew)
  hethet = hetfirst * ((m-1)/popnew) * (0.75)
  hetrec = hetfirst * (n/popnew) * (0.5)
  hettotal = hetdom + hethet + hetrec

  #if selecting recessive first
  recfirst = n/pop
  recdom = recfirst * k/popnew
  rechet = recfirst * m/popnew * (0.5)
  rectotal = recdom + rechet

  return dom + hettotal + rectotal




