def all_perms(elements):
  if len(elements) <= 1:
    yield elements
  else:
    for perm in all_perms(elements[1:]):
      for i in range(len(elements)):
        yield perm[:i] + elements[0:1] + perm[i:]

def perm(n):
  nums = [x for x in range(1,n+1)]

  perms = all_perms(nums)
  perm_strings = []

  for perm in perms:
    new_string = " ".join(map(str, perm))
    perm_strings.append(new_string)

  fout = open("out.txt","w")
  fout.write(str(len(perm_strings)) + '\n')
  for i in perm_strings:
    fout.write(i + '\n')
  fout.close()