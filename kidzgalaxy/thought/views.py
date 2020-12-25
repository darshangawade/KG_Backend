from django.shortcuts import render
from . import urls

from datetime import datetime
from time import gmtime, strftime
# Create your views here.
from .models import Thought


def index(request):
    thought=Thought.objects.all()
    showtime = strftime("%d-%b", gmtime())
    return render(request,'index.html',{'thought':thought,'showtime':showtime})


