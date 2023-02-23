from django.shortcuts import render
from django.http import HttpResponse
from Resto.models import *
from Resto.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

def inicioSesion(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user= authenticate(username = usuario, password = contra)

            if user:

                login(request, user)

                return render(request, "Resto/inicio.html", {"mensaje":f"Bienvenidos a Sabores Latinos ** {user} **"})
            
        else:

            return render(request, "Resto/inicio.html", {"mensaje":"Datos incorrectos"})
        
    else:

        form = AuthenticationForm()

    return render(request, "Resto/login.html", {"formulario":form})

def registro(request):

    if request.method == "POST":

        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "Resto/inicio.html", {"mensaje":"Usuario creado."})
    
    else:

        form = UsuarioRegistro()

    return render(request, "Resto/registro.html", {"formulario": form})

@login_required
def editarUsuario(request):

    usuario = request.user

    if request.method == "POST":

        form = FormularioEditar(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()
            return render(request, "Resto/inicio.html")
        
    else:

        form = FormularioEditar(initial = {"email": usuario.email, "first_name": usuario.first_name, "last_name":usuario.last_name})
    
    return render(request, "Resto/editarPerfil.html", {"formulario":form, "usuario":usuario})


def inicio(request):
    return render(request, "Resto/inicio.html")

def about(request):
   return render(request,"Resto/about.html")

def Registro(request):
    return render(request, "Resto/registro.html")

def Reserva(request):
    return render(request, "Resto/reservacion.html")

def carta(request):
    return render(request, "Resto/menu.html")


def choice_sucursal(request):
    if request.method == "POST":

        formulario2= escoger_Sucursal(request.POST)
        if formulario2.is_valid():

            info = formulario2.cleaned_data

            nciudad= Sucursal(Ciudad= info["Ciudad"])

            nciudad.save()
        
            return render(request,"Resto/inicio.html")
        
    else:
        formulario2 = escoger_Sucursal()

    return render(request, "Resto/sucursal.html", {"form2" : formulario2})

@login_required
def creacion_reserva(request):
    if request.method == "POST":

        formulario3= genera_reserva(request.POST)
        if formulario3.is_valid():

            info = formulario3.cleaned_data

            nreserva= Reservacion(nombre= info["nombre"], DNI= info["DNI"], numero_mesa= info["numero_mesa"], num_invitados= info["num_invitados"], fecha_de_reservacion= info["fecha_de_reservacion"])

            nreserva.save()
        
            return render(request,"Resto/inicio.html")
        
    else:
        formulario3 = genera_reserva()

    return render(request, "Resto/reservacion.html", {"form3" : formulario3})


@login_required
def busqueda_reserva(request):

    return render(request, "Resto/inicio.html")

@login_required
def resultados_reservas(request):

    if request.GET["nombre"]:

        nombre= request.GET["nombre"]
        reserva= Reservacion.objects.filter(nombre__icontains = nombre)

        return render(request, "Resto/inicio.html" , {"reserva":reserva, "nombre": nombre})
    
    else:

        respuesta= "No Enviastes Datos"

    return HttpResponse(respuesta)

@login_required
def agregarAvatar(request):

    if request.method == "POST":

        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():

            usuarioActual = User.objects.get(username= request.user)

            avatar = Avatar(usuario= usuarioActual, imagen= form.cleaned_data["imagen"])

            avatar.save()

            return render(request, "Resto/inicio.html")
        
    else:

        form = AvatarFormulario()

    return render(request, "Resto/agregarAvatar.html", {"formulario": form})




class ListaReserva(ListView):

    model = Reservacion
    template_name = "Resto/reservacion_list.html"

class DetalleReserva(DetailView):

    model = Reservacion
    template_name = "Resto/reservacion_detail.html"

class CrearReserva(CreateView):

    model = Reservacion
    success_url = "/Resto/reservacion/list"
    fields = ["nombre", "DNI", "numero_mesa", "num_invitados", "fecha_de_reservacion"]

class ActualizarReserva(UpdateView):

    model = Reservacion
    success_url = "/Resto/reservacion/list"
    fields = ["nombre", "DNI", "numero_mesa", "num_invitados", "fecha_de_reservacion"]

class BorrarReserva(DeleteView):

    model = Reservacion
    success_url = "/Resto/reservacion/list"







    