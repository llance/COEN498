from shelvedApp.dbOperations import addDataToDB, multi_dimensions
import discogs_client

__author__ = 'v_bilodeau'

#Set up discogs client, with key auth
d = discogs_client.Client('shelved/0.1', user_token='vbJueTnrwORBYqihcMCUjUylzyiDsQpKWvbunjik')

#Gets a UPC code
def queryDiscogs(upc, user='books'):
    request = d.search(str(upc))
    if (len(request) > 0):
        data = multi_dimensions(2)
        album = request[0]
        artists = []
        for artist in album.artists:
            artists.append(artist.name)
        title = album.title
        physicalMedium = album.formats[0]['name']
        numDisks = album.formats[0]['qty']
        label = album.labels[0].name
        """
        tracklisting is experimental
        tracklist = {}
        for track in album.tracklist:
            tracklist[track.data['position']]['title'] = track.title
            tracklist[track.data['position']]['duration'] = track.data['duration']
        #import pdb; pdb.set_trace()
        """

        data[str(upc)]['title'] = title
        data[str(upc)]['artists'] = artists
        data[str(upc)]['numDisks'] = numDisks
        data[str(upc)]['physicalMedium'] = physicalMedium
        data[str(upc)]['label'] = label
        #data[str(upc)]['tracklist'] = tracklist

        media_type = 'music'

        addDataToDB(media_type, data, user)

        return str(title)

    else:
        empty_dict = {}
        return empty_dict