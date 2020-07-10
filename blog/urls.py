from django.urls import *

import blog.views

url=[
    path("hello world",blog.views.hello)
]