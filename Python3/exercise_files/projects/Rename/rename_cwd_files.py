import os
folder = os.getcwd()
find = input("Enter extinsion to Find: ").lower()
replace = input("Enter extension to Replace: ")

for filename in os.listdir(folder):
  infilename = os.path.join(folder,filename)
  if not os.path.isfile(infilename):
    continue
  oldbase = os.path.splitext(filename)[1]
  newname = infilename.replace(find, replace)
  output = os.rename(infilename, newname)
  print(f"\t{filename} renamed:")
print("The task has been completed....")

# # to findout file by extension
'''
oldbase = os.path.splitext(filename)[1].lower() in filename
'''