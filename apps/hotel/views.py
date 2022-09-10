from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from apps.hotel.models import *
from apps.hotel.forms import *
from django.views.generic import *

#-------------------------------------------
# Vistas Del Model Hotel

class HotelLista(ListView):
    model = Hotel
    template_name = 'hotel/hotel_lista.html'

class HotelDetalle(DetailView):
    model = Hotel
    template_name = 'hotel/detalle.html'

class HotelEditar(UpdateView):
    model = Hotel
    template_name = 'hotel/hotel_form.html'
    form_class = HotelFormulario
    success_url = reverse_lazy('lista')

class HotelCrear(CreateView):
    model = Hotel
    template_name = 'hotel/hotel_form.html'
    form_class = HotelFormulario
    success_url = reverse_lazy('lista')

class HotelEliminar(DeleteView):
    model = Hotel
    template_name = 'hotel/hotel_eliminar.html'
    success_url = reverse_lazy('lista')

#--------------------------------------------
# Vistas Del Modelo Unidad

class UnidadFormulario(CreateView):
    model = Unidad
    template_name = 'unidad/unidad_form.html'
    form_class = UnidadForm
    success_url = reverse_lazy('lista')

class UnidadEditar(UpdateView):
    model = Unidad
    template_name = 'unidad/unidad_form.html'
    form_class = UnidadForm
    success_url = reverse_lazy('lista')

class UnidadLista(ListView):
    model = Unidad
    template_name = 'unidad/unidad_lista.html'

class UnidadEliminar(DeleteView):
    model = Unidad
    template_name = 'unidad/unidad_eliminar.html'
    success_url = reverse_lazy('lista')
