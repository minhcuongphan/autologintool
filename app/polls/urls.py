from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('login-ajax', views.autologin, name="auto_login")
]