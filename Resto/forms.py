from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Resto.models import Avatar



class registrar(forms.Form):
    nombre = forms.CharField(max_length=60)
    DNI = forms.CharField()
    telefono = forms.IntegerField()


ARG = 'Buenos Aires Argentina'
PER = 'Lima Peru'
COL = 'Bogota Colombia'
BRA = 'Sao Paulo Brasil'

sucursales = [
        (ARG, 'Buenos Aires Argentina'),
        (PER, 'Lima Peru'),
        (COL, 'Bogota Colombia'),
        (BRA, 'Sao Paulo Brasil')
    ]
class escoger_Sucursal(forms.Form):

    Ciudad = forms.ChoiceField(choices=sucursales,widget=forms.Select, initial=ARG)
    

class genera_reserva(forms.Form):
    nombre= forms.CharField(max_length=60)
    DNI= forms.CharField(max_length=10)
    numero_mesa = forms.IntegerField()
    num_invitados = forms.IntegerField()
    fecha_de_reservacion = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contrasena", widget=forms.PasswordInput)
    password1 = forms.CharField(label = "Repetir Contrasena", widget=forms.PasswordInput)

    class Meta:

        model= User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class FormularioEditar(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contrasena", widget=forms.PasswordInput)
    password1 = forms.CharField(label = "Repetir Contrasena", widget=forms.PasswordInput)

    class Meta:

        model= User
        fields = ["email", "first_name", "last_name", "password1", "password2"]

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model= Avatar
        fields = ["imagen"]






