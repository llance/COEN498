__author__ = 'vbilodeau'

import datetime
import requests
from django.utils import timezone
import json
from apiclient.discovery import build

#Set up app key
books_service = build('books', 'v1', developerKey='AIzaSyD6P55381pkncIFbOvxP-Ov0sYt-lcoOP8')

# gets a UPC OR ISBN
def queryGoogle(isbn):
    query = str(isbn)
    request = books_service.volumes().list(source='public', q=query)
    books = request.execute()

    print("book is :", books)
    if (books['items'][0]):
        book = books["items"][0]
        title = (book["volumeInfo"]["title"])
        #find a faster streamlined less retarded way
        if (book["volumeInfo"]["subtitle"]):
            subtitle = (book["volumeInfo"]["subtitle"])
        authors = (book["volumeInfo"]["authors"])
        pageCount = (book["volumeInfo"]["pageCount"])
        publisher = (book["volumeInfo"]["publisher"])
        publishedDate = (book["volumeInfo"]["publishedDate"])
        language = (book["volumeInfo"]["language"])

