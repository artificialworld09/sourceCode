import os
path = os.listdir('.')
path.remove('change_extension.py')
replace = '.mp5'
for i in path:
	o = i
	s = os.path.splitext(i)
	l = list(s)
	l.pop(-1)
	for j in l:
		data = j + replace
		os.rename(o, data)
		print('\tConverting:', o, '->',data)
print("Task Done")