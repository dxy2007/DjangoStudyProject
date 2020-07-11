from django.urls import *

import blog.views

urlpatterns=[
    path("",blog.views.hello_world)

]