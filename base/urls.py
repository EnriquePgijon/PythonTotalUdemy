from django.urls import path
from .views import ListaPendientes,DetalleTarea,CrearTarea,EditarTarea, EliminarTarea,Logueo,PaginaRegistro
from django.contrib.auth.views import LogoutView
urlpatterns = [path('',ListaPendientes.as_view(),name='tareas'),
               path('login/',Logueo.as_view(),name='login'),
               path('registro/', PaginaRegistro.as_view(), name='registro'),
               path('logout/',LogoutView.as_view(next_page="login"),name='logout'),
               path('Tarea/<int:pk>',DetalleTarea.as_view(),name='Tarea'),
               path('crear-tarea/',CrearTarea.as_view(),name='Crear-tarea'),
               path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea'),
               path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar-tarea')
               ]

