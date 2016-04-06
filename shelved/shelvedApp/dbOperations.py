__author__ = 'vbilodeau'

from pymongo import MongoClient, InsertOne
from collections import defaultdict, Counter

def addDataToDB(media_type, data, user='books'):
    #print('inserting info for isbn :', str(isbn), 'into MongoDB')
    user = user
    data['type'] = media_type
    myMongoClient = MongoClient()
    myMongoDb = myMongoClient.myMongoDb
    collection = myMongoDb[user]
    requests = [InsertOne(data)]
    result = collection.bulk_write(requests)
    print('result from writing to MongoDb was ', result)

def deleteItem(uniqueIdetifier, user='books'):
  return 0

#Creates an n-dimension dictionary where the n-th dimension is of type 'type'  
def multi_dimensions(n):
  type = Counter
  if n<=1:
    return type()
  return defaultdict(lambda:multi_dimensions(n-1))

def find_items(key, value, user='books'):
  myMongoClient = MongoClient()
  myMongoDb = myMongoClient.myMongoDb
  collection = myMongoDb[user]
  results = []
  for result in collection.find({key:value}):
    data = result['data']
    for key in data:
      if type(data[key]) is list:
        listdata = data[key]
        stringedData = ",".join(listdata)
        data[key] = stringedData

    results.append(data)

  return results

