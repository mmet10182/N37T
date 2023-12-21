from django.urls import path
from . import views

urlpatterns = [
    path('get_cookies/', views.get_cookies, name='get_cookies'),
]