# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import MySQLdb
import MySQLdb.cursors

db = MySQLdb.connect(host='127.0.0.1', user='root', passwd='52332580', db='douban', port=3306, charset='utf8',
					 cursorclass=MySQLdb.cursors.DictCursor)
db.autocommit(True)
cursor = db.cursor()

#fr = open('data/douban_movie_clean.txt', 'r')

# Create
# count = 0
# for line in fr:
# 	count += 1
# 	# print count
# 	if count == 1:
# 		continue
# 	line = line.strip().split('^')
# 	# print line
# 	cursor.execute("insert into movie(title,url,rate,length,description) VALUES (%s,%s,%s,%s,%s)",
# 				   [line[1], line[2], line[4], line[-3], line[-1]])
#
# fr.close()

# Update
# cursor.execute("update movie set title=%s,url=%s where id=1",['xuefliang','www.google'])

# Read
# cursor.execute("select * from movie")
# movies=cursor.fetchall()
#
# print len(movies)
# print movies[0]

# Delete
cursor.execute("delete from movie where id=%s",[1])

cursor.close()
db.close()
