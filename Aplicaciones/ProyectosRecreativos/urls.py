from django.urls import path
from . import views

urlpatterns = [

    path('',views.inicio, name='inicio'),


    path('Cliente/agregarCliente/',views.agregarCliente,name='agregarCliente'),
    path('Cliente/listado_cliente/',views.listado_cliente,name='listado_cliente'),
    path('Cliente/guardarCliente/', views.guardarCliente, name='guardarCliente'),
    path('Cliente/editar_cliente/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('Cliente/eliminarCliente/<int:cliente_id>/', views.eliminarCliente, name='eliminarCliente'),

    path('Contratista/agregarContratista/',views.agregarContratista,name='agregarContratista'),
    path('Contratista/listado_contratista/',views.listado_contratista,name='listado_contratista'),
    path('Contratista/guardarContratista/', views.guardarContratista, name='guardarContratista'),
    path('Contratista/editar_contratista/<int:contratista_id>/', views.editar_contratista, name='editar_contratista'),
    path('Contratista/eliminarContratista/<int:contratista_id>/', views.eliminarContratista, name='eliminarContratista'),

    path('ParqueRecreativo/agregarParque/', views.agregarParque, name='agregarParque'),
    path('ParqueRecreativo/listado_parques/', views.listado_parques, name='listado_parques'),
    path('ParqueRecreativo/guardarParque/', views.guardarParque, name='guardarParque'),
    path('ParqueRecreativo/editar_parque/<int:parque_id>/', views.editar_parque, name='editar_parque'),
    path('ParqueRecreativo/eliminarParque/<int:parque_id>/', views.eliminar_parque, name='eliminar_parque'),

    path('ProyectoConstruccion/agregar/', views.agregar_proyecto, name='agregar_proyecto'),
    path('ProyectoConstruccion/listado/', views.listado_proyectos, name='listado_proyectos'),
    path('ProyectoConstruccion/guardar/', views.guardar_proyecto, name='guardar_proyecto'),
    path('ProyectoConstruccion/editar/<int:proyecto_id>/', views.editar_proyecto, name='editar_proyecto'),
    path('ProyectoConstruccion/eliminar/<int:proyecto_id>/', views.eliminar_proyecto, name='eliminar_proyecto'),

]