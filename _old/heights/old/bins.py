def bins():
  with open("rosalind_bins.txt") as myfile:
    head = [next(myfile) for x in xrange(4)]
  myfile.close()

  stringArray = head[2].replace('\n', '')  
  array = []
  for word in stringArray.split():
    array.append(int(word))

  stringInts = head[3].replace('\n', '')  
  ints = []
  for word in stringInts.split():
    ints.append(int(word))

  results = []

  for i in ints:
    x=0
    y=len(array)-1
    while(True):
      if y<x:
        results.append(-1)
        break
      else:
        mid = (x+y)/2
        if array[mid] > i:
          y = mid-1
        elif array[mid] < i:
          x = mid+1
        elif array[mid] == i:
          results.append(mid+1)
          break  

  fout = open('out.txt','w')
  for i in results:
    fout.write(str(i) + " ")
  fout.close()

