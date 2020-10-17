from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register,name='accounts'),
    path('login', views.login,name='accounts'),
    ]
