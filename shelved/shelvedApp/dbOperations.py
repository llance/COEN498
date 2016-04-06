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


def multi_dimensions(n):
  """ Creates an n-dimension dictionary where the n-th dimension is of type 'type'
  """
  type = Counter
  if n<=1:
    return type()
  return defaultdict(lambda:multi_dimensions(n-1))