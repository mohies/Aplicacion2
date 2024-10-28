from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

#Filtramos una lista de usuarios que esten participando en cada torneo
def lista_torneo(request):
    torneos = Torneo.objects.prefetch_related("torneoparticipante_set__participante__usuario").all() # El sufijo _set se utiliza en Django para acceder a las relaciones inversas de modelos relacionados mediante claves foráneas cuando no se ha especificado un related_name suele ser en los modelos intermedios en relaciones de muchos a muchos.
    return render(request, 'torneo/lista_torneo.html', {'torneos': torneos})

 # Filtramos los participantes con más de 100 puntos obtenidos y los ordenamos por fecha de inscripción de manera descendente
def lista_participantes(request):
    participantes = Participante.objects.select_related("usuario").filter(puntos_obtenidos__gt=100).order_by('-fecha_inscripcion')
    return render(request, 'torneo/lista_participantes.html', {'participantes': participantes})

# Filtrar usuarios que tienen una clasificación y que están en los primeros lugares
def lista_usuarios_primeros(request):
    usuarios_primeros = Usuario.objects.filter(clasificacion__ranking__gte=0).order_by("clasificacion__ranking").prefetch_related('clasificacion')
    return render(request, 'torneo/lista_usuarios_primeros.html', {'usuarios_primeros': usuarios_primeros})
# views.py
from django.shortcuts import render
from .models import Participante

# Vista que filtra participantes con más de 100 puntos y que hayan ganado al menos un torneo
def participantes_con_puntos_y_ganados(request):
    # Filtro con AND entre puntos de participante y torneos ganados en la clasificación
    participantes = Participante.objects.filter(
        puntos_obtenidos__gt=100,
        usuario__clasificacion__torneos_ganados__gt=0  # Relación reversa desde Usuario hacia Clasificacion
    ).prefetch_related('usuario__clasificacion')
    return render(request, 'torneo/participantes_con_puntos_y_ganados.html', {'participantes': participantes})

def torneos_sin_participantes(request):
    # Filtra torneos donde no hay ninguna relación en la tabla intermedia
    torneos = Torneo.objects.filter(torneoparticipante__participante=None)
    
    return render(request, 'torneo/torneos_sin_participantes.html', {'torneos': torneos})