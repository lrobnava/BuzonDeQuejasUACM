from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('buzondequejas/', views.BuzonQuejas, name='buzondequejas'),
    path('Queja/', views.Queja, name='Queja')
]