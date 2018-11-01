import pymongo
import time
from hdfs.client import Client
import pyhdfs

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient["music"]
mycol = mydb["zjComments"]

hdfs_url = "http://127.0.0.1:50070"
client = Client(hdfs_url, root="/")
client.makedirs("/test2")
hdfsclient = pyhdfs.HdfsClient(hosts="127.0.0.1:50070", user_name="hadoop")
# 返回这个用户的根目录
j=0
result=mycol.find({},{'content':1,'time':1,'_id': 0})
#result=mycol.find({})
commentsList=list(result)
##for item in commentsList:
##    print(item)
#count=len(commentsList)
#print(count)

i = 0
path=""
for item in commentsList:
    itemJson = str(item) + "\n"
    if i % 50 == 0:
        now = time.time()
        #com = item['content'] + '\t' + str(item['time'])
        path='/test2/' + 'content' + str(now) + '.log'
        #hdfsclient.create(path, str(com+'\r').encode("utf-8"))
        hdfsclient.create(path, itemJson.encode("utf-8"))
    else:
        #com = item['content'] + '\t' + str(item['time'])
        hdfsclient.append(path, itemJson.encode("utf-8"))
        #if i % 50== 49
        #  time.sleep(3)
    i += 1






