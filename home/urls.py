from django.urls import path, include
from home import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('services/', include('services.urls'),name='services'),
    path('blog/', include('blog.urls'),name='blog'),
    path('contact/', views.contact, name="contact"),
    path('profile/', views.profile, name="profile"),
    path('about/', views.about, name="about"),
    path('search/', views.search, name="search"),
    path('signup/', views.handleSignUp, name="handleSignUp"),
    path('login/', views.handeLogin, name="handleLogin"),
    path('logout/', views.handelLogout, name="handleLogout"),
    path('profile/', views.profile, name="profile"),
    path('profile/<slug>/', views.user, name="user"),
    path('profile/editProfile/', views.editProfile, name="editProfile"),
    path('profile/confirmdeleteaccount/', views.confirmdeleteaccount, name="confirmdeleteaccount"),
    path('profile/confirmdeleteaccount/deleteaccount/', views.deleteaccount, name="deleteaccount"),
]

# if settings.DEBUG:
#     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)