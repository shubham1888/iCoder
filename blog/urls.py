from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('postComment/', views.postComment, name="postComment"),
    path('', views.blogHome, name="bloghome"),
    path('writeBlog/', views.writeBlog, name="writeBlog"),
    path('<str:slug>/', views.blogPost, name="blogPost"),
    path('blog/{{post.slug}}/author/', views.author, name="author"),
]
