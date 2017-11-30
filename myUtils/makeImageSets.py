f = open('parse_result.txt', 'r')
lines = f.readlines()

file_names = ['airplane', 'antelope', 'bear', 'bicycle', 'bird', 'bus', 'car', \
 'cattle', 'dog', 'cat', 'elephant', 'fox', 'giant_panda', 'hamster', 'horse', \
 'lion', 'lizard', 'monkey', 'motorcycle', 'rabbit', 'red_panda', 'sheep', 'snake', \
 'squirrel', 'tiger', 'train', 'turtle', 'watercraft', 'whale', 'zebra']

codes = ['n02691156', 'n02419796', 'n02131653', 'n02834778', 'n01503061', 'n02924116', \
	'n02958343', 'n02402425', 'n02084071', 'n02121808', 'n02503517', 'n02118333', 'n02510455', \
	'n02342885', 'n02374451', 'n02129165', 'n01674464', 'n02484322', 'n03790512', 'n02324045', \
	'n02509815', 'n02411705', 'n01726692', 'n02355227', 'n02129604', 'n04468005', 'n01662784', \
	'n04530566', 'n02062744', 'n02391049']

for j in range(30):
	fn = file_names[j] + '_test.txt'
	imset = open(fn, 'w')
	for i in range(8000, 11165):
		n = str(i+1).zfill(6)
		if codes[j] in lines[i].split():
			check = ' 1\n'
		else:
			check = ' -1\n'
		imset.write(n + check) 
	imset.close()
f.close()
