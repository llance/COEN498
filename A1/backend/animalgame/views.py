from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse

# from django.shortcuts import render
# from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.

@csrf_exempt
def test(request):
    if request.method == 'GET':
        return render(request, 'index.html')



def test2(request):
    if request.method == 'GET':
        print('user clicked yes ');
        return HttpResponse("hello world",status=200)
        #return render(request, 'test.html')

def test3(request):
    if request.method == 'GET':
        print("user clicked no");
        return HttpResponse("why you lyin",status=200)