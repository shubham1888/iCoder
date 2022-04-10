from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blogHome, name="bloghome"),
    path('<str:slug>/', views.blogPost, name="blogPost"),
    path('postComment/', views.postComment, name="postComment"),
    path('writeBlog/', views.writeBlog, name="writeBlog"),
]
