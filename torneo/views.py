from django.shortcuts import render
from .models import *
from django.db.models import Prefetch,Count,Q
# Create your views here.
def index(request):
    return render(request, 'index.html')

#Filtramos una lista de usuarios que esten participando en cada torneo
def lista_torneo(request):
    torneos = Torneo.objects.prefetch_related("participantes").all() # El sufijo _set se utiliza en Django para acceder a las relaciones inversas de modelos relacionados mediante claves foráneas cuando no se ha especificado un related_name suele ser en los modelos intermedios en relaciones de muchos a muchos.
    return render(request, 'torneo/lista_torneo.html', {'torneos': torneos})

 # Filtramos los participantes con más de 100 puntos obtenidos y los ordenamos por fecha de inscripción de manera descendente
def lista_participantes(request):
    participantes = Participante.objects.select_related("usuario").filter(puntos_obtenidos__gt=100).order_by('-fecha_inscripcion')
    return render(request, 'torneo/lista_participantes.html', {'participantes': participantes})

# Filtrar usuarios que tienen una clasificación y que están en los primeros lugares
def lista_usuarios_primeros(request):
    usuarios_primeros = Usuario.objects.filter(jugador__ranking__gte=0).order_by("jugador__ranking").select_related('jugador')
    return render(request, 'torneo/lista_usuarios_primeros.html', {'usuarios_primeros': usuarios_primeros})
# views.py

# Vista que filtra participantes con más de 100 puntos y que hayan ganado al menos un torneo
def participantes_con_puntos_y_ganados(request):
    # Filtro con AND entre puntos de participante y torneos ganados en la clasificación
    participantes = Participante.objects.filter(
        puntos_obtenidos__gt=100,
        usuario__jugador__torneos_ganados__gt=0  # Relación reversa desde Usuario hacia Clasificacion
    ).prefetch_related("usuario__jugador").select_related("usuario")
    return render(request, 'torneo/participantes_con_puntos_y_ganados.html', {'participantes': participantes})

def torneos_sin_participantes(request):
    # Filtra torneos donde no hay ninguna relación en la tabla intermedia
    torneos = Torneo.objects.filter(torneoparticipante=None).all()
    #al no querer mostrar ningun dato de la tabla participante no es necesario hacer ningun prefetch y luego a la hora de filtrar none tenemos que poner la tabla no un atributo para no tener problemas
    return render(request, 'torneo/torneos_sin_participantes.html', {'torneos': torneos})


#Filtra el numero de consolas de los participantes en un torneo
def consolas_participantes(request,participante_id):
    participantes = Participante.objects.filter(id=participante_id).aggregate(num_consolas=Count('torneoparticipante__torneo__juegos_torneo__id_consola'))
    return render(request, 'torneo/consolas_participantes.html', {'total_consolas': participantes})

#Filtra el estado torneo de un juego
def estado_torneojuego(request):
    torneojuegos = TorneoJuego.objects.filter(Q(estado="activo") | Q(estado="pendiente")).select_related("torneo","juego") 
    return render(request, 'torneo/estado_torneojuego.html', {'torneojuegos': torneojuegos})

# Vista para mostrar los primeros 5 torneos por fecha de inicio
def primeros_torneos(request):
    torneos = Torneo.objects.order_by('fecha_inicio')[:5]  # Limita a los primeros 5
    return render(request, 'torneo/primeros_torneos.html', {'torneos': torneos})