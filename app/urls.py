from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
  
    path('register/',registerview.as_view()),
    path('login/',loginview.as_view()),
     path('posts/',postview.as_view()),
     path('postdetail/<int:pk>/',postdetailview.as_view())
]