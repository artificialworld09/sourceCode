import os

def rename(path, new_name, numbering, extension):
	list = os.listdir(path) # fetch all the files from directory
	os.chdir(path) # Goto that directory
	
	# Business logic using loop using loop
	count = numbering
	for i in list:
		os.rename (i, new_name+str(count)+'.'+extension)
		count += 1

path = r"C:\Users\Administrator\Desktop\New folder"
rename(path, "Photo", 1, "jpg")