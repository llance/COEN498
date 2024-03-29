__author__ = 'lanceli'

from amazon.api import AmazonAPI

from shelvedApp.dbOperations import addDataToDB, multi_dimensions


#revised method using the simple amazon api
def queryAmazon(upc, user='books'):
    print('queryAmazon called')
    amazon = AmazonAPI('AKIAIQOSMQ3XYLJ2OWOQ','xBV4OLH9/OorIXGHhUzyeSkPuQGnME/QVQsKQfGS', 'shelvedWebApp')
    try:
        data = multi_dimensions(2)
        product = amazon.lookup(IdType='UPC', ItemId=upc , SearchIndex='All')
        #print('results is', results)
        #product = results[0]
        #print('product is ', product)
        title = product.title #title, include "(format)"
        productFormat = product.binding #explicit format type "blu-ray" or "dvd"
        data['upc'] = str(upc)
        data['data']['title'] = title
        data['data']['productFormat'] = productFormat
        data['data']['upc'] = str(upc)
        media_type = 'movie'

        addDataToDB(media_type, data, user)

        return str(title)

    except:
        empty_dict = {}
        return empty_dict


