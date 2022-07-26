from django.urls import path
from blogApp import views
from blogApp.views import *

urlpatterns = [
   path('login', views.login, name= 'login'),
   path('inicio', views.inicio, name='inicio'),



]