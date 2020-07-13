from django.urls import path
from Jiawem.views import test,home

urlpatterns = [
  path('',test,name= 'Jiawem'),
  path('home',home,name="home"),
]