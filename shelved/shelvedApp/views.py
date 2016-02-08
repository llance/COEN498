# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

def play(request):
    if request.method == 'GET':
        print('user clicked yes ');

        return HttpResponse("hello world",status=200)
