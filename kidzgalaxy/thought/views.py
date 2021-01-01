from django.core import serializers
from django.http import JsonResponse, HttpResponse

from django.shortcuts import render
from rest_framework.renderers import JSONRenderer

from . import urls
import json

from datetime import datetime
from time import gmtime, strftime
# Create your views here.
from .models import Thought
from .serializers import ThoughtSerializer


def index(request):
        quotes = 'NULL'
        showtime = strftime("%d-%b", gmtime())
        print(showtime)
        thought=Thought.objects.get(thought_date=showtime)
        serializer = ThoughtSerializer(thought)
        return JsonResponse(serializer.data)






    #json_data = JSONRenderer().render(serializer.data)
    #print(json_data)
    #return HttpResponse(JSONRenderer().render(json_data))


    #return render(request, 'index.html', {'thought': quotes, 'showtime': showtime})
    #thoughts=list(thought)
    #print(thoughts)

    #post_list = serializers.serialize('json', thought)
    #print(post_list)
    #return JsonResponse(post_list,safe=False)
    #return JsonResponse(list(Thought.objects.all().values()),safe=False)


    #return JsonResponse({'thought':thought,'showtime':showtime},safe=True)
    # return HttpResponse({'thought':thought,'showtime':showtime}, mimetype="application/json")



