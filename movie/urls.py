# coding=utf-8

from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_view),
    path('index/', views.movie_index_view)
]
