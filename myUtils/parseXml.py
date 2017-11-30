from xml.etree.ElementTree import parse

fw = open('parse_result.txt', 'w')

cnt = 0
for i in range(11165):
	n = str(i+1).zfill(6)
	tree = parse(n + '.xml')
	anno = tree.getroot()
	object_tags = anno.findall('object')
	object_names = ' '
	if object_tags==[]:
		object_names = ' none'
		cnt = cnt + 1
	else:
		for object_tag in object_tags:
			object_names = object_names + object_tag.findtext('name') + ' '
	fw.write(n + object_names + '\n')

fw.close()

print cnt
