from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
    now = datetime.now()
    html = ''
    return HttpResponse('Hello world, here is polls index')


