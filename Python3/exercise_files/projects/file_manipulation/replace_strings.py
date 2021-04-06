import os
find = ".in"
replace = ".com"
path = r"C:\Users\Administrator\Desktop\test"
source = os.listdir(path)

for file in source:
  inputfile = os.path.join(path, file)
  print("Conversion is going for: " + inputfile)
  with open(inputfile, "r") as input:
    filedata = input.read()
    freq = 0
    freq = filedata.count(find)
  destination = os.path.join(path, file)
  filedata = filedata.replace(find, replace)
  with open(destination, "w") as file:
    file.write(filedata)
print(f"Total Record Replaced: {freq}")