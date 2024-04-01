from django.urls import path
from app2.views import *
app_name='something'

urlpatterns=[
    path('h1/',h1,name='h1'),
]