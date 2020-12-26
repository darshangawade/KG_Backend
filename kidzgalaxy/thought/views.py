from django.core import serializers
from django.http import JsonResponse, HttpResponse

from django.shortcuts import render
from . import urls
import json

from datetime import datetime
from time import gmtime, strftime
# Create your views here.
from .models import Thought


def index(request):
    thought=Thought.objects.all()
    showtime = strftime("%d-%b", gmtime())

    post_list = serializers.serialize('json', thought)
    # print(post_list)
    # return JsonResponse(post_list,safe=False)
    #return JsonResponse(list(Thought.objects.all().values()), safe=False)

    #return JsonResponse(json.dumps({'thought':thought,'showtime':showtime}))
    # return HttpResponse({'thought':thought,'showtime':showtime}, mimetype="application/json")
    return render(request,'index.html',{'thought':thought,'showtime':showtime})


