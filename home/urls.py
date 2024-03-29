from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('blog/', include('blog.urls'),name='blog'),
    path('contact/', views.contact, name="contact"),
    path('profile/', views.profile, name="profile"),
    path('search/', views.search, name="search"),
    path('signup/', views.handleSignUp, name="handleSignUp"),
    path('login/', views.handeLogin, name="handleLogin"),
    path('logout/', views.handelLogout, name="handleLogout"),
    path('profile/', views.profile, name="profile"),
    path('profile/changepassword/', views.changepassword, name="changepassword"),
    path('profile/addtodo/', views.addtodo, name="addtodo"),
    path('profile/<str:username>/', views.username, name="username"),
    path('profile/confirmdeleteaccount/', views.confirmdeleteaccount, name="confirmdeleteaccount"),
    path('profile/confirmdeleteaccount/deleteaccount/', views.deleteaccount, name="deleteaccount"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)