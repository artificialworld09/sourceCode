import os, shutil
path = ('.')
replace = 'txt'
leave = ('html', 'py')
for c, folders, files in os.walk(path):
     for file in files:
     	if file == 'change_extension_recursive.py':
     		continue
     	if file.endswith(leave):
     		continue
     	old = file
     	data1 = os.path.join(c, old)
     	s = os.path.splitext(file)
     	l = list(s)
     	l.pop(-1)
     	for i in l:
     		new = i+'.'+replace
	     	data2 = os.path.join(c, new)
	     	os.rename(data1, data2)
	     	print('\tConverting:', old, '->', new)
print("Task Done")