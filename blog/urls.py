from django.urls import *

import blog.views

url=[
    path("hello_world",blog.views.hello_world)

]