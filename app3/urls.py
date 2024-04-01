from django.urls import path
from app3.views import *
app_name='nothing'

urlpatterns=[
    path('h2/',h2,name='h2'),
]