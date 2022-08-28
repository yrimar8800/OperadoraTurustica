from django.urls import path
from apps.usuarios.views import *

urlpatterns = [
    path('registro/', Registrousuario.as_view(), name='registro')
]