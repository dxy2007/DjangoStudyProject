from django.shortcuts import render

from django.http import *

# Create your views here.

def hello_world(requust):
    return HttpResponse("Hello World")
