from django.contrib import admin
from django.urls import path
from .import views
from django.urls import include

urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
]