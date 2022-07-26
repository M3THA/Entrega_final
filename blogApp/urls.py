from django.urls import path
from blogApp import views
from blogApp.views import *

urlpatterns = [
   path('login', views.login_usuario, name= 'login'),
   path('inicio', views.inicio, name='inicio'),



]