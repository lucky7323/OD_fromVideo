import numpy as np
import os

path = './JPEGImages/VID/train/'
#path = './Annotations/VID/train/'

folders = ['a/', 'b/', 'c/']

for i in range(3):
	fold = folders[i]
	print('Start to remove files in (' + fold + ') ')
	for root1, dirs1, files1 in os.walk(path + fold):
		for idx, dir in enumerate(sorted(dirs1)):
			if idx%100==0:
				print(str(idx) + ' iter - Start to remove files in (' + fold + dir + ')')
			for root, dirs, files in os.walk(path + fold + dir +'/'):
				size = len(files)
				a = size / 5
				for file in sorted(files):
					fnum = file.split('.')
					fnum = fnum[0]
					if int(fnum)!=1 and int(fnum)!=1+a and int(fnum)!=1+(2*a) \
						and int(fnum)!=1+(3*a) and int(fnum)!=1+(4*a):
						os.remove(path + fold + dir + '/' + file)



































