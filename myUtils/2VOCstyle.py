import numpy as np
import os
import shutil

path = './JPEGImages/VID/train/'
#path = './Annotations/VID/train/'

folders = ['a/', 'b/', 'c/']

cnt = 1
for i in range(3):
	fold = folders[i]
	print('Start to remove files in (' + fold + ') ')
	for root1, dirs1, files1 in os.walk(path + fold):
		for idx, dir in enumerate(sorted(dirs1)):
			if idx%100==0:
				print(str(idx) + ' iter - Start to remove files in (' + fold + dir + ')')
			for root, dirs, files in os.walk(path + fold + dir +'/'):
				for file in sorted(files):
					origin = (path + fold + dir + '/' + file)
					cnt_str = str(cnt).zfill(6)
					dest = './JPEGImages/%s' %cnt_str
					dest += '.jpg'
					shutil.copy(origin, dest)
					cnt = cnt + 1


































