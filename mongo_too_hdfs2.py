#!/usr/bin/python
# -*- coding :utf-8 -*-
import time
import pymongo
import sys
import io
import os
mongo_url = "localhost:27017"
client = pymongo.MongoClient(mongo_url)
DATABASE = "mafengwo"
db = client.get_database(DATABASE)
COLLECTION = "travel"
db_coll = db.get_collection(COLLECTION)
cursor = db_coll.find()
#只查询日本
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
			f1 = open("F:\simulate-hdfs\\"+english + str(now) + '.log', 'a', encoding='utf-8')
			f1.write(item)
			f1.write('\n')

			print(item)
			i = i + 1
		else:
			f1.write(item)
			f1.write('\n')

			print(item)
			i = i + 1
			print(i)
	f1.close()
	time.sleep(29)

findcountry("日本",'Japan')
findcountry("青海",'Qinghai')
findcountry("泰国",'Thailand')
findcountry("英国",'UK')
findcountry("瑞士",'Swiss')
# time.sleep(200)
'''
def notecountry(country,english):
	coun=db_coll.find({'country':country},{'note':1,'_id':0})
	listcoun=list(coun)
	i=0
	for line in listcoun:


		note= line['note']
		if i == 0:
			now = time.time()
			f1 = open("F:\simulate-hdfs\\note"+english + str(now) + '.log', 'a', encoding='utf-8')
			f1.write(note)
			f1.write('\n')

			print(note)
			i = i + 1
		else:
			f1.write(note)
			f1.write('\n')
			print(note)
			i = i + 1
			print(i)
	f1.close()
	time.sleep(3)
notecountry("日本",'Japan')
notecountry("青海",'Qinghai')
notecountry("泰国",'Thailand')
notecountry("英国",'UK')
notecountry("瑞士",'Swiss')
'''
'''
Japan=db_coll.find({'country':'日本'},{'_id':0})
listJAPAN=list(Japan)
i=0
for line in listJAPAN:
	title = line['title'].strip()
	# print(type(title))
	a = line['note'].strip
	note=str(a)
	# print(type(note))
	date = line['time'].strip()
	people = line['people'].strip()
	cost = line['cost'].strip()
	day = line['day'].strip()
	country=line['country'].strip()
	comment=line['comment'].strip()
	browse=line['browse'].strip()
	item=title+'@@'+note+'@@'+date+'@@'+people+'@@'+cost+'@@'+day+'@@'+country+'@@'+comment+'@@'+browse
	if i==0:
		now=time.time()
		f1 = open("F:\simulate-hdfs\\japan" + str(now) + '.log', 'a', encoding='utf-8')
		f1.write(item)
		print(item)
		i=i+1
	else:
		f1.write(item)
		print(item)
		i=i+1
		print(i)
'''
# # 只查询mfw
# query=db_coll.find({},{'_id':0})
# #print(list(query))
# a=list(query)
# # print(a)
# i=0
# for line in a:
#
# 	if i%5000==0:
# 		now =time.time()
# 		#print(now)
# 		f1=open("F:\simulate-hdfs\\travel"+str(now)+'.log','a',encoding='utf-8')
# 		#f2 = open("F:\simulate-hdfs\\note" + str(now) + '.log', 'a', encoding='utf-8')
# 		title = line['title'].strip()
# 		note=line['note'].strip()
# 		date=line['time'].strip()
# 		people=line['people'].strip()
# 		cost=line['cost'].strip()
# 		day=line['day'].strip()
# 		print(people+'@@'+cost+'@@'+day)
# 		f1.write(people+'@@'+cost+'@@'+day)
# 		f1.write('\n')
# 		# f2.write(note+'\n')
# 		i=i+1
# 		print(i)
# 	else:
# 		title = line['title'].strip()
# 		note = line['note']
# 		date = line['time'].strip()
# 		people = line['people'].strip()
# 		cost = line['cost'].strip()
# 		day = line['day'].strip()
# 		print(people + '@@' + cost + '@@' + day)
# 		f1.write(people + '@@' + cost + '@@' + day)
# 		f1.write('\n')
# 		# f2.write(note + '\n')
# 		i = i + 1
# 		print(i)
# 		if i%5000==0:
# 			time.sleep(1)