import os

p = os.listdir()
for i in p:
	s = i.split(".")[-1]
	print(s)
#s = p.split(".")[-1]
