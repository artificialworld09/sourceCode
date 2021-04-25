import os
path = '.'
source = os.listdir(path)
find ='Artificial World'
replace = 'Abdul'

class Edit:
  def __init__(self, path, source, find, replace):
    self.path = path
    self.source = source
    self.find = find
    self.replace = replace
    
  def mani(self):
    freq = 0
    for file in self.source:
      inputfile = os.path.join(self.path, file)
      if not os.path.isdir(file):
        if file == 'file_editor.py':
          continue
        print("Conversion is going for >>", file)
        with open(inputfile, mode="r", encoding="utf-8") as input:
          filedata = input.read()
          freq += filedata.count(find)
        destination = os.path.join(path, file)
        filedata = filedata.replace(find, replace)
        with open(destination, mode="w", encoding="utf-8") as file:
          file.write(filedata)
    print(f"Total Record Replaced: {freq}")
      
f = Edit(path, source, find, replace)
f.mani()