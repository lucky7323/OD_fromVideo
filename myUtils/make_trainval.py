import numpy as np
import os

fw = open('trainval.txt', 'w')
for i in range(8000):
	name = str(i+1).zfill(6)
	fw.write(name+'\n')

fw.close()
