import os

f = open('./empty_frame.txt', 'r')
lines = (f.read()).split()

cnt = 0
for name in lines:
	try:
		os.remove('./' + name + '.xml')
	except:
		cnt = cnt + 1

print cnt
f.close()
