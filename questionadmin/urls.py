from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="index"),
    path('additem/',Additem, name="Additem"),
    path('delete/<str:id>/',delete, name="delete"),
    path('edit/<str:id>/',edit, name="edit"),
]
