import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

fr = open("data/xyj.txt", "r")

characters = []
stat = {}

for line in fr:
	line = line.split()

	if len(line) == 0:
		continue

	# print type(line)

	temp = json.dumps(line, encoding="UTF-8", ensure_ascii=False)
	result = [t for t in temp][2:-2]

	for x in xrange(0, len(result)):
		if not result[x] in characters:
			characters.append(result[x])

		if not stat.has_key(result[x]):
			stat[result[x]]=0
		stat[result[x]]+=1
fr.close()

stat=sorted(stat.iteritems(),key=lambda d:d[1],reverse=True)

for x in xrange(0,20):
	print characters[x]

print '*' *20

for x in xrange(0,20):
	print stat[x][0],stat[x][1]


