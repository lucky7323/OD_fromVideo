import os

empty = open('./empty_frame.txt', 'r')
emptys = empty.read().split()

file_names = ['airplane', 'antelope', 'bear', 'bicycle', 'bird', 'bus', 'car', \
	'cattle', 'dog', 'cat', 'elephant', 'fox', 'giant_panda', 'hamster', 'horse', \
    'lion', 'lizard', 'monkey', 'motorcycle', 'rabbit', 'red_panda', 'sheep', 'snake', \
	'squirrel', 'tiger', 'train', 'turtle', 'watercraft', 'whale', 'zebra']

for i in range(30):
	with open('./' + file_names[i] + '_trainval.txt', 'r+') as f:
		lines = []
		for line in f:
			if line.split()[0] not in emptys:
				lines = lines + [line]
			else:
				print line.split()[0]
		f.seek(0)
		f.writelines(lines)
		f.truncate()

empty.close()
