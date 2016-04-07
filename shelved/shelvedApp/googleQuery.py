__author__ = 'vbilodeau'

from apiclient.discovery import build
from shelvedApp.dbOperations import addDataToDB, multi_dimensions

#Set up app key
books_service = build('books', 'v1', developerKey='AIzaSyD6P55381pkncIFbOvxP-Ov0sYt-lcoOP8')

# gets a UPC OR ISBN
def queryGoogle(isbn, user='books'):
    query = str(isbn)
    request = books_service.volumes().list(source='public', q=query)
    books = request.execute()
    data = multi_dimensions(2)
    fields = ['title', 'authors', 'subtitle', 'pageCount', 'publisher', 'publishedDate', 'language']

    try:
        book = books["items"][0]['volumeInfo']
        data['isbn'] = query
        data['data']['isbn'] = query
        for key in fields:
            if key in book:
                #print "the key is : " + str(key) + " and the book[key] = " + str(book[key])
                data['data'][key] = book[key]

        print("title is :", str(book['title'])) 

        media_type = 'book'

        addDataToDB(media_type, data, user)

        #print("result of mongo write is :", result)

        return str(book['title'])
        # print("authors is :", authors)
        # print("pageCount is :", pageCount)
        # print("publisher is :", publisher)
        # print("publishedDate is :", publishedDate)
        # print("language is :", language)
    except:
        empty_dict = {}
        return empty_dict
