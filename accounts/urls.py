from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tickets',views.tickets, name='tickets'),
    path('agregarTicket',views.crearTicket, name='agregarTicket')
]