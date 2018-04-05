def ints_to_ascii(ints):
  ints = ints.split(',')
  output = ''
  
  for i in ints:
    output += str(unichr(i))

  print(output)
  