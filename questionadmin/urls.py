from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/',index, name="adminindex"),
    path('',login_user, name="login"),
    path('',logout_user, name="logout"),
    path('additem/',Additem, name="Additem"),
    path('delete/<str:id>/',delete, name="delete"),
    path('edit/<str:id>/',edit, name="edit"),
]
