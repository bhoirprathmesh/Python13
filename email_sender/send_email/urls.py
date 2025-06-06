from django.urls import path
from . import views
from .views import send_email

urlpatterns = [
    path('', views.index),
    path('send-email/', send_email, name='send_email')
]