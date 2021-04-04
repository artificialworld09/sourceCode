import os
path = os.listdir('.')
path.remove('rename.py')
n = len(path)
fileName ='Image'
fileExt = 'jpg'

for i in range(n):
	old = path[i]
	new = fileName+'-'+str(i)+'.'+fileExt
	if os.path.isfile(old):
		os.rename(old, new)
		print('\tConverting:', old, '->',new)
print("Task Done")