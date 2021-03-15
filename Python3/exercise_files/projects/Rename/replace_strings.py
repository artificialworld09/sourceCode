import os
texttofind = ".in"
texttoreplace = ".com"
path = r"C:\Users\Administrator\Desktop\test"
dest = r"C:\Users\Administrator\Desktop\test"
sourcepath = os.listdir(path)
for file in sourcepath:
  inputfile = os.path.join(path, file)
  print("Conversion is going for: " + inputfile)
  with open(inputfile, "r") as inputfile:
    filedata = inputfile.read()
    freq = 0
    freq = filedata.count(texttofind)
  destinationpath = os.path.join(path, file)
  filedata = filedata.replace(texttofind, texttoreplace)
  with open(destinationpath, "w") as file:
    file.write(filedata)
print(f"Total Record Replaced: {freq}")