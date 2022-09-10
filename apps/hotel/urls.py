from django.urls import path
from apps.hotel.views import *

urlpatterns = [
    #------ Urls Hotel ------
    path('lista/', HotelLista.as_view(), name='lista'),
    path('detalle/<pk>/', HotelDetalle.as_view(), name='detalle'),
    path('crear/', HotelCrear.as_view(), name='crear'),
    path('editar/<pk>/', HotelEditar.as_view(), name='editar'),
    path('eliminar/<pk>/', HotelEliminar.as_view(), name='eliminar'),

    #------ URLS Unidad ------
    path('crear_unidad/', UnidadFormulario.as_view(), name='crear_unidad'),
    path('listar_unidad/', UnidadLista.as_view(), name='listar_unidad'),
    path('editar_unidad/<pk>/', UnidadEditar.as_view(), name='editar_unidad'),
    path('eliminar_unidad/<pk>/', UnidadEliminar.as_view(), name='eliminar_unidad'), 
]
