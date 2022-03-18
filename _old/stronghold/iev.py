def iev():
  with open("rosalind_iev.txt") as myfile:
    head = [next(myfile) for x in xrange(1)]
  
  nums = head[0].replace('\n', '').split()
  nums = map(float,nums)

  for i in nums: 
    print i

  nextpop = 0
  for i in range(len(nums)-1):
    prob = 1.0
    if i==3:
      prob = 0.75
    elif i==4:
      prob = 0.5 
    nextpop += 2 * nums[i] * prob

  print nextpop