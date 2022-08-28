from django import forms
from apps.hotel.models import *

class HotelFormulario(forms.ModelForm):
    class Meta:
        model = Hotel

        fields = [
            'nombre',
            'ubucacion',
            'descripcion',
            'servicio_hotel',
        ]


        labels = {
            'nombre': 'Nombre',
            'ubucacion': 'Ubicacion',
            'descripcion': 'Descripcion',
            'servicio_hotel': 'Servicios del Hotel',
        }

        widgets = {
            'nombre': forms.TextInput(),
            'ubucacion': forms.TextInput(),
            'descripcion': forms.TextInput(),
            'servicio_hotel': forms.CheckboxSelectMultiple(),
        }


class UnidadForm(forms.ModelForm):
    class Meta:
        model = Unidad

        fields = [
            'numero_unidad',
            'piso',
            'servicio_unidad',
            'hotel',
        ]


        labels ={
            'numero_unidad': 'Numero De Unidad',
            'piso': 'Piso De La Unidad',
            'servicio_unidad':'Servicios De La Unidad' ,
            'hotel': 'Hotel',
        }

        widgets = {
            'numero_unidad': forms.TextInput(),
            'piso': forms.TextInput(),
            'servicio_unidad': forms.CheckboxSelectMultiple(),
            'hotel': forms.Select(),
        }