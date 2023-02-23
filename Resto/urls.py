from django.urls import path
from . import views
from Resto.views import *
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('about/', about, name = 'Acercademi' ), 
    path('registro/', Registro, name = 'Registro' ),
    path('reserva/', Reserva, name = 'Reserva'),
    path('register/', registro, name = 'Registros'),
    path('nueva_sucursal/', choice_sucursal, name = 'Nueva sucursal'),
    path('nueva_reserva/', creacion_reserva, name= 'Nueva Reserva'),
    path('buscar_reserva/', busqueda_reserva, name= 'BuscarReserva'),
    path('resultados/', resultados_reservas, name= 'Resultados'),
    path('login/', inicioSesion, name= 'Login'),
    path('logout/', logout_then_login , name= 'Logout'),
    path('editar/', editarUsuario , name= 'EditarUsuario'),
    path('agregar/', agregarAvatar , name= 'Avatar'),
    path('construction/', carta, name='Menu'),
   



    #CRUD PARA RESERVAS
    
    path('reservacion/list/', login_required(ListaReserva.as_view()), name= 'ReservaLeer'),
    path('reservacion/<int:pk>/', DetalleReserva.as_view(), name= 'Detail'),
    path('nueva_reserva', creacion_reserva, name= 'nueva Reserva'),
    path('reservacion/editar/<int:pk>/', login_required(ActualizarReserva.as_view()), name= 'Edit'),
    path('reservacion/borrar/<int:pk>/', login_required(BorrarReserva.as_view()), name= 'Delete'),

    
    
]
