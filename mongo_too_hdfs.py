#!/usr/bin/python
# -*- coding :utf-8 -*-
#!/usr/bin/python
# -*- coding :utf-8 -*-

import pymongo
import time
from hdfs.client import Client
import pyhdfs

mongo_url = "localhost:27017"
client = pymongo.MongoClient(mongo_url)
DATABASE = "mafengwo"
db = client.get_database(DATABASE)
COLLECTION = "travel"
db_coll = db.get_collection(COLLECTION)


hdfs_url = "http://127.0.0.1:50070"
client = Client(hdfs_url, root="/")
client.makedirs("/test")
hdfsclient = pyhdfs.HdfsClient(hosts="127.0.0.1:50070", user_name="hadoop")
# 返回这个用户的根目录

cursor = db_coll.find()

def findcountry(country,english):
	coun=db_coll.find({'country':country},{'_id':0})
	listcoun=list(coun)
	i=0
	for line in listcoun:

		title = line['title'].strip()

		# print(type(title))
		note= line['note']
		date = line['time'].strip()
		people = line['people'].strip()
		cost = line['cost'].strip()
		day = line['day'].strip()
		country = line['country'].strip()
		comment = line['comment'].strip()
		browse = line['browse'].strip()
		item = title + '@@'  + date + '@@' + people + '@@' + cost + '@@' + day + '@@' + country + '@@' + comment + '@@' + browse
		if i == 0:
			now = time.time()
			path = '/test/' + 'english' + str(now) + '.log'
			# hdfsclient.create(path, str(com+'\r').encode("utf-8"))
			hdfsclient.create(path, item.encode("utf-8"))


			print(item)
			i = i + 1
		else:
			hdfsclient.append(path, item.encode("utf-8"))

			print(item)
			i = i + 1
			print(i)
	time.sleep(29)

findcountry("日本",'Japan')
findcountry("青海",'Qinghai')
findcountry("泰国",'Thailand')
findcountry("英国",'UK')
findcountry("瑞士",'Swiss')



'''
import time
import pymongo
import sys
import io
import os
mongo_url = "localhost:27017"
client = pymongo.MongoClient(mongo_url)
DATABASE = "mfw"
db = client.get_database(DATABASE)
COLLECTION = "mafengwo"
db_coll = db.get_collection(COLLECTION)
cursor = db_coll.find()
# 只查询head
query=db_coll.find({},{'_id':0})
#print(list(query))
a=list(query)
# print(a)
i=0
for line in a:

	if i%5000==0:
		now =time.time()
		#print(now)
		f1=open("F:\simulate-hdfs\peplecostday"+str(now)+'.log','a',encoding='utf-8')
		f2 = open("F:\simulate-hdfs\\note" + str(now) + '.log', 'a', encoding='utf-8')
		title = line['title'].strip()
		note=line['note'].strip()
		date=line['time'].strip()
		people=line['people'].strip()
		cost=line['cost'].strip()
		day=line['day'].strip()
		print(people+'@@'+cost+'@@'+day)
		f1.write(people+'@@'+cost+'@@'+day)
		f1.write('\n')
		f2.write(note+'\n')
		i=i+1
		print(i)
	else:
		title = line['title'].strip()
		note = line['note']
		date = line['time'].strip()
		people = line['people'].strip()
		cost = line['cost'].strip()
		day = line['day'].strip()
		print(people + '@@' + cost + '@@' + day)
		f1.write(people + '@@' + cost + '@@' + day)
		f1.write('\n')
		f2.write(note + '\n')
		i = i + 1
		print(i)
		if i%5000==0:
			time.sleep(0.1)
# time.sleep(2)
# os.makedirs('F:\software\stop-spark')
'''