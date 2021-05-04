import os
path = '.'
source = os.listdir(path)
find = '-'
replace = '_'
count = 0

for file in source:
  f1 = file.lower()
  data = os.path.join(path, f1)
  r = f1.replace(find, replace)
  print('Conversion is going to: ', file, '>>', r)
  os.rename(data, r)
print(count)