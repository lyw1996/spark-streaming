#!/usr/bin/python
# -*- coding :utf-8 -*-
import pymongo
import re
client = pymongo.MongoClient(host='127.0.0.1', port=27017)
db = client.mafengwo
collection = db.travel

f1=open('F:\simulate-hdfs\\Qinghai1540739636.871133.log','r',encoding='utf-8')
for line in f1:
	lena=len(line.split('@@'))
	a=line.split('@@')[4]
	if a!='':
		a=a.split(' 天')[0]
		print(a)
# 	if lena!=8:
# 		print(line.split('@@')[0])
# 		print('\n')

# a=collection.find({'title':'英国🇬🇧'})
# a=collection.find('day':re.compile('天'))
# collection.update({'title':'在泰国的日子'},{'day':'5 天'})
# print(list(a))