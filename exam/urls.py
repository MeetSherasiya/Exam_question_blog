from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="index"),
    path('questionbank/<str:pk>/<str:pk1>/<str:pk2>/<str:pk3>/<str:pk4>/<str:pk5>/',question, name="question"),
    path('questionbank/<str:pk>/<str:pk1>/<str:pk2>/<str:pk3>/<str:pk4>/',subject, name="subject"),
    path('questionbank/<str:pk>/<str:pk1>/<str:pk2>/<str:pk3>/',examtype, name="examtype"),
    path('questionbank/<str:pk>/<str:pk1>/<str:pk2>/',sem, name="semester"),
    path('paper/<str:pk>/',paper, name="paper"),
    path('questionbank/<str:pk>/<str:pk1>/',branch, name="branch"),
    path('questionbank/<str:pk>/',field, name="field"),
]

