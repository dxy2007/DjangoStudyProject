from django.shortcuts import render

from django.http import *

# Create your views here.

html = '<h1>Hello World</h1>'


def hello_world(request):
    return HttpResponse(html)
