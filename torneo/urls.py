from django.urls import path, re_path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('torneo/lista',views.lista_torneo,name='lista_torneo'),
    path('torneo/lista_participantes',views.lista_participantes,name='lista_participantes'),
    path('usuarios/primeros/', views.lista_usuarios_primeros, name='lista_usuarios_primeros'),
    path('participantes/puntos_y_ganados/', views.participantes_con_puntos_y_ganados, name='participantes_con_puntos_y_ganados'),
     path('torneos_sin_participantes/', views.torneos_sin_participantes, name='torneos_sin_participantes'),

]