from django.urls import path
from .import views

urlpatterns = [
    path('', views.logIn),
    path('logIn', views.logIn, name = 'logIn'),
    path('home', views.home, name = 'home'),
    path('logout', views.logOut, name = 'logout')
]