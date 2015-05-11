def grph():
  strings = {}

  fin = open("rosalind_grph.txt")

  identifier = ""
  data = ""

  for line in fin:
    line = line.replace('\n', '')
    if line[0] == '>':
      if data != "":
        strings[data] = identifier
        identifier = ""
        data = ""
      identifier = line[1:]
    else:
      data += line
  fin.close()

  for i, j in strings.items():
    print i
    print j

  edge_list = []

  for start, start_ID in strings.items():
    for end, end_ID in strings.items():
      if start[-3:] == end[:3] and start_ID != end_ID:
        edge_list.append( (strings[start], strings[end]) )

  fout = open("out.txt","w")
  for (a,b) in edge_list:
    fout.write(a + " " + b + "\n")
  fout.close()

if __name__ == '__main__':
  grph()