from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# from django.shortcuts import render
# from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.

@csrf_exempt
def test(request):
    if request.method == 'GET':
        return HttpResponse(json.dumps("hello world!"), content_type="applicationn/json")