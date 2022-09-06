from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from apps.usuarios.models import *
from apps.usuarios.views import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import *
from apps.usuarios.forms import *

from django.contrib.auth.views import *


#----------------------------------------------
# Vistas Del Modelo Usuarios

class Registrousuario(CreateView):
    model = User
    template_name = 'usuarios/usuarios_form.html'
    form_class = RegistroForm
    success_url = reverse_lazy('lista')

class SingOutView(LogoutView):
    success_url = reverse_lazy('lista')
    pass


