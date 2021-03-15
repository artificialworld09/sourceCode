import os

directory = os.getcwd() #get the working directory of script.
find = input("Enter word to find: ")
replace = input("Enter word to Replace: ")

for subdir, dirs, files in os.walk(directory):
  for filename in files:
    if filename.find(find) > 0:
      subdirectoryPath = os.path.relpath(subdir, directory) #get the path to your subdirectory
      filePath = os.path.join(subdirectoryPath, filename) #get the path to your file
      if not os.path.isfile(filePath):
        continue
      newFilePath = filePath.replace(find,replace) #create the new name
      os.rename(filePath, newFilePath) #rename your file
      print(f"\t{filename} renamed:")
print("The task has been completed....")