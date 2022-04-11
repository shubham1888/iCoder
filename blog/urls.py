from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('writeBlog/', views.writeBlog, name="writeBlog"),
    path('', views.blogHome, name="bloghome"),
    path('<str:slug>/', views.blogPost, name="blogPost"),
    path('/blog/postComment/', views.postComment, name="postComment"),
]
