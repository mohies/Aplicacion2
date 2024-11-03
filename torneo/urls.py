from django.urls import path, re_path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('torneo/lista',views.lista_torneo,name='lista_torneo'),
    path('torneo/lista_participantes',views.lista_participantes,name='lista_participantes'),
    path('usuarios/primeros/', views.lista_usuarios_primeros, name='lista_usuarios_primeros'),
    path('participantes/puntos_y_ganados/', views.participantes_con_puntos_y_ganados, name='participantes_con_puntos_y_ganados'),
    path('participantes/consolas/<int:participante_id>/', views.consolas_participantes, name='consolas_participantes'),
    path('estado/torneojuego/', views.estado_torneojuego, name='estado_torneojuego'), 
    path('primeros-torneos/', views.primeros_torneos, name='primeros_torneos'),
    re_path(r'^usuarios/noclasificados//?$', views.usuarios_noclasificados, name='usuarios_noclasificados'), # una barra al final que puede ser opcional
    path('torneo/<int:torneo_id>/participantes/<str:estado>/', views.participantes_por_torneo_y_estado, name='participantes_por_torneo_y_estado'),
    path('espectadores/nombre/<str:nombre>/', views.espectadores_por_nombre, name='espectadores_por_nombre'),

]