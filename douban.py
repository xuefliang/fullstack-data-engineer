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
