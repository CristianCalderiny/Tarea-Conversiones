from django.urls import path
from . import views

app_name = 'conversor'

urlpatterns = [
    path('', views.convertir_binario, name='convertir'),
]