from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', index),
    path('registrar_reserva', register_reserva),
    path('crear', create),
    path('editar_reserva/<str:id_reserva>', edit),
    path('actualizar_reserva/<str:id_reserva>', update),
    path('borrar_reserva/<str:id_reserva>', delete),
]
