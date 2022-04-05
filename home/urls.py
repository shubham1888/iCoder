from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('blog/', include('blog.urls'),name='blog'),
    path('contact/', views.contact, name="contact"),
    path('profile/', views.profile, name="profile"),
    path('about/', views.about, name="about"),
    path('search/', views.search, name="search"),
    path('signup/', views.handleSignUp, name="handleSignUp"),
    path('login/', views.handeLogin, name="handleLogin"),
    path('logout/', views.handelLogout, name="handleLogout"),
    path('profile/<str:slug>/', views.profile, name="profile"),
]