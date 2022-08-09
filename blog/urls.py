from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('pessoal/', views.sobre),
    path('profissional/', views.profissional)
]
