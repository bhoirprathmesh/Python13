from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('counter', views.counter),
    path('largest', views.largest)
]