__author__ = 'vbilodeau'

from apiclient.discovery import build
from pymongo import MongoClient, InsertOne
from collections import defaultdict
from collections import Counter


#Set up app key
books_service = build('books', 'v1', developerKey='AIzaSyD6P55381pkncIFbOvxP-Ov0sYt-lcoOP8')

# gets a UPC OR ISBN
def queryGoogle(isbn):
    query = str(isbn)
    request = books_service.volumes().list(source='public', q=query)
    books = request.execute()

    if (books['items'][0]):
        book = books["items"][0]
        title = (book["volumeInfo"]["title"])
        authors = (book["volumeInfo"]["authors"])
        #find a faster streamlined less retarded way
        # if (book["volumeInfo"]["subtitle"]):
        #     subtitle = (book["volumeInfo"]["subtitle"])
        #     authors = (book["volumeInfo"]["authors"])
        #     pageCount = (book["volumeInfo"]["pageCount"])
        #     publisher = (book["volumeInfo"]["publisher"])
        #     publishedDate = (book["volumeInfo"]["publishedDate"])
        #     language = (book["volumeInfo"]["language"])

        print("title is :", title)

        addDataToDB(isbn, title, authors)

        #print("result of mongo write is :", result)

        return title
        # print("authors is :", authors)
        # print("pageCount is :", pageCount)
        # print("publisher is :", publisher)
        # print("publishedDate is :", publishedDate)
        # print("language is :", language)


def addDataToDB(isbn, title, author):
    print('inserting info for isbn :', str(isbn), 'into MongoDB')
    myMongoClient = MongoClient()
    myMongoDb = myMongoClient.myMongoDb

    data = multi_dimensions(2, Counter)


    data[str(isbn)]['title'] = title
    data[str(isbn)]['author'] = author

    requests = [InsertOne(data)]
    result = myMongoDb.books.bulk_write(requests)
    print('result from writing to MongoDb was ', result)


def multi_dimensions(n, type):
  """ Creates an n-dimension dictionary where the n-th dimension is of type 'type'
  """
  if n<=1:
    return type()
  return defaultdict(lambda:multi_dimensions(n-1, type))
