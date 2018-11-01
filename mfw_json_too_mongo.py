import pymongo
client = pymongo.MongoClient(host='127.0.0.1', port=27017)
db = client.mafengwo
collection = db.travel
def too_mongo():
    # 本地json文件路径
    import json
    with open("F:\研一上\云计算\第一次实践作业\mafengwo_copy1.json", 'r',encoding='utf-8') as f:
        items = json.loads(f.read())
        for item in items['RECORDS']:
            # title = item['title']
            note = item['note']
            print(type(note))
            print(note)
            # time = item['time']
            # people = item['people']
            # cost = item['cost']
            # day = item['day']
           # collection.insert_one({'title':item['title'],'note':item['note'],'time':item['time'],'people':item['people'],'cost':item['cost'],'day':item['day'],'country':item['country'],'comment':item['comment'],'browse':item['browse']})

# client = pymongo.MongoClient(host='127.0.0.1', port=27017)
# db = client.mfw
# collection = db.mafengwo
# def too_mongo():
#     # 本地json文件路径
#     import json
#     with open("/Users/yangguang/PycharmProjects/import_sql/mafengwo.json", 'r') as f:
#         items = json.loads(f.read())
#         for item in items['RECORDS']:
#             # title = item['title']
#             # note = item['note']
#             # time = item['time']
#             # people = item['people']
#             # cost = item['cost']
#             # day = item['day']
#             collection.insert({'title':item['title'],'note':item['note'],'time':item['time'],'people':item['people'],'cost':item['cost'],'day':item['day']})


if __name__ == '__main__':
    too_mongo()
