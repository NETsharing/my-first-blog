"""djangogirls URL Configuration


"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('post/', views.post_trust),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    url(r'^$', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new')
]
