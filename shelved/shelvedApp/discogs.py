from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

__author__ = 'lanceli'

@csrf_exempt
def discogs(request):
    if request.method == 'GET':
        print("discogs called")

        d = discogs_client.Client('ExampleApplication/0.1')
        results = d.search('Stockholm By Night', type='release')
        print("results.pages is : " + results.pages)
        artist = results[0].artists[0]
        print("artist.name is : " + artist.name)
        return HttpResponse("hello",status=200)





        # consumer_key = 'MEkvKirNCzRPMeSFAvPz'
        # consumer_secret = 'DbpYOkkRJwMLBlpPSMVRlccnexYJqVIA'
        #
        # request_token_url = 'https://api.discogs.com/oauth/request_token'
        # authorize_url = 'https://www.discogs.com/oauth/authorize'
        # access_token_url = 'https://api.discogs.com/oauth/access_token'
        #
        #
        # user_agent = 'my_secret_discogs_api_example/2.0'
        #
        # consumer = oauth.Consumer(consumer_key, consumer_secret)
        # client = oauth.Client(consumer)
        #
        # resp, content = client.request(request_token_url, 'POST', headers={'User-Agent': user_agent})
        #
        # if resp['status'] != '200':
        #     sys.exit('Invalid response {0}.'.format(resp['status']))
        #
        # request_token = dict(urlparse.parse_qsl(content))
        #
        #
        # discogsclient = discogs_client.Client(user_agent)
        # discogsclient.set_consumer_key(consumer_key, consumer_secret)
        #
        # token, secret, url = discogsclient.get_authorize_url()
        #
        #
        # print(' == Request Token == ')
        # print('    * oauth_token        = {0}'.format(token))
        # print('    * oauth_token_secret = {0}'.format(secret))
        #
        #
        # #user = discogsclient.identity()
        #
        # search_results = discogsclient.search('House For All', type='release',artist='Blunted Dummies')
        # print("foo3" + str(search_results))
        #
        #
        # for release in search_results:
        #     print('\n\t== discogs-id {id} =='.format(id=release.id))
        #     print(u'\tArtist\t: {artist}'.format(artist=', '.join(artist.name for artist in release.artists)))
        #     print(u'\tTitle\t: {title}'.format(title=release.title))
        #     print(u'\tYear\t: {year}'.format(year=release.year))
        #     print(u'\tLabels\t: {label}'.format(label=','.join(label.name for label in release.labels)))

        # print("helloworld" + str(results))
        # print("helloworld1" + str(results[0]))
        # for stuff in results:
        #     print ("stuff is : " + str(stuff))
        #
        # artist = results[0].artists[0]
        # print("artist.name" + str(artist.name))