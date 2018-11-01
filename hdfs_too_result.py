#!/usr/bin/python
# -*- coding :utf-8 -*-
from operator import add
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark import SparkConf
import os
import time

def updateFunction(newValues, runningCount):
    if runningCount is None:
        runningCount = 0
    return sum(newValues, runningCount)

def savepeoplefile(x):
	with open("F:\\result\People.csv" , 'a+', encoding='utf-8') as f:
		f.write(str(x[0]))
		f.write(',')
		f.write(str(x[1]))
		f.write('\n')
	return

def savecostfile(x):
	with open("F:\\result\Cost.csv" , 'a+', encoding='utf-8') as f:
		f.write(str(x[0]))
		f.write(',')
		f.write(str(x[1]))
		f.write('\n')
	return

def savedayfile(x):
	with open("F:\\result\Day.csv" , 'a+', encoding='utf-8') as f:
		f.write(str(x[0]))
		f.write(',')
		f.write(str(x[1]))
		f.write('\n')
	return

if __name__ == "__main__":
	conf = SparkConf().setMaster('local[2]').setAppName('streaming')
	sc = SparkContext(conf=conf)
	ssc = StreamingContext(sc, 20)
	lines = ssc.textFileStream('F:\simulate-hdfs')
	#人均费用
	Cost = lines.filter(lambda x: x.split('@@')[3] != '')
	Cost2 = Cost.map(lambda x: (x.split('@@')[5], int(x.split('@@')[3].split('RMB')[0])))
	CostAverage = Cost2.reduceByKey(lambda x, y: (x + y) / 2)
	CostAverage.pprint()
	CostSave=CostAverage.map(lambda x:savecostfile(x))
	CostSave.pprint(0)
	#出游天数
	Day = lines.filter(lambda x: x.split('@@')[4] != '')
	Day2 = Day.map(lambda x: (x.split('@@')[5], int(x.split('@@')[4].split(' 天')[0])))
	DayAverage = Day2.reduceByKey(lambda x, y: (x + y) / 2)
	DayAverage.pprint()
	DaySave=DayAverage.map(lambda x:savedayfile(x))
	DaySave.pprint(0)
	#人员
	People = lines.filter(lambda x: x.split('@@')[2] != '')
	People2 = People.map(lambda x: (x.split('@@')[2], 1))
	PeopleAll = People2.reduceByKey(add)
	PeopleAll.pprint()
	PeopleSave=PeopleAll.map(lambda x:savepeoplefile(x))
	PeopleSave.pprint(0)

	# time.sleep(5)
	# if os.path.exists("F:\\result\People.txt")==True:
	# 	os.remove("F:\\result\People.txt")



	# PeopleCounts = PeopleAll.updateStateByKey(updateFunction)
	# # PeopleCounts=PeopleAll.reduceByKey(lambda x:print(type(x)))
	# PeopleCounts.pprint()
	#
	# ssc.checkpoint('/spark/ssc')
	ssc.start()
	ssc.awaitTermination()

# lines=sc.textFile('F:\simulate-hdfs\\UK1540736079.4866624.log')
# ab=lines.collect()
# for a in ab:
# 	lena=len(a.split('@@'))
# 	if lena!=8:
# 		print(a)
# cost

# day

# mfw
# conf=SparkConf().setMaster('local[2]').setAppName("third1")
# sc = SparkContext(conf=conf)
# ssc = StreamingContext(sc,60)
# # lines = ssc.textFileStream('hdfs://localhost:9000/test')
# lines = ssc.textFileStream('F:\simulate-hdfs')
# words = lines.filter(lambda x:x.split('@@')[1]!='').map(lambda x:(x.split('@@')[0],int(x.split('@@')[1].split('RMB')[0])))
# wordCounts = words.reduceByKey(lambda x,y:(x+y)/2)
# wordCounts.pprint()

# wordCounts.repartition(1).saveAsTextFiles('F:\\result\cost')






# lines = sc.textFile('hdfs://localhost:9000/test/travel1540708925.6132672.log')
# words = lines.filter(lambda x:x.split('@@')[1]!='').map(lambda x:(x.split('@@')[0],int(x.split('@@')[1].split('RMB')[0])))
# wordCounts = words.reduceByKey(lambda x,y:(x+y)/2)
# print(wordCounts.collect())


