# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#print sys.getdefaultencoding()

import urllib
import urllib2
import json
from bs4 import BeautifulSoup

tags=[]
url='https://movie.douban.com/j/search_tags?type=movie'

request=urllib2.Request(url=url)
response=urllib2.urlopen(request,timeout=20)
result=json.loads(response.read())

tags=result['tags']
movies=[]
for tag in  tags:
    limit=0
    while 1:
        url='https://movie.douban.com/j/search_subjects?type=movie&tag='+tag+'&sort=recommend&page_limit=20&page_start='+str(limit)
        request = urllib2.Request(url=url)
        response = urllib2.urlopen(request, timeout=20)
        result = json.loads(response.read())

        result=result['subjects']

        if len(result)==0:
            break

        limit+=20
        for item in result:
            movies.append(item)

for x in xrange(0,4):
    item=movies[x]
    request=urllib2.Request(url=item['url'])
    response=urllib2.urlopen(request,timeout=20)
    result=response.read()
    html=BeautifulSoup(result)
    title=html.select('h1')[0].select('span')[0].get_text()
    print title

    movies[x]['title']=title

    keys=html.select("#info span.pl")
    #values=html.select('#info span.attrs')

    for i in xrange(0,len(keys)):
        print keys[i].get_text()
        #print values[i].get_text()

fw=open('data/movies.txt','w')

for item in movies:
    tmp=''
    for key,value in item.items():
        tmp+=str(value)+','
    fw.write(tmp[:-1]+'\r\n')
fw.closed()
