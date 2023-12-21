from django.urls import path
from . import views

urlpatterns = [
    path('get_console_jnlp', views.get_console_jnlp, name='get_console_jnlp'),
]