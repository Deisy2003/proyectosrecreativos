from django.shortcuts import render,  redirect, get_object_or_404
from django.contrib import messages

from .models import Cliente, Contratista, ParqueRecreativo, ProyectoConstruccion
from decimal import Decimal

def inicio(request):
    return render(request,'inicio.html')

def agregarCliente(request):
    cliente = Cliente.objects.all()  
    return render(request, 'Cliente/agregarCliente.html', { 'cliente': cliente})


def listado_cliente(request):
    cliente = Cliente.objects.all()
    return render(request, 'Cliente/listado_cliente.html', {'cliente': cliente})


def guardarCliente(request):
    if request.method == "POST":
        cedula = request.POST.get('cedula')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')

        nuevo_cliente = Cliente(
            cedula=cedula,
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            email=email,
            direccion=direccion
        )
        nuevo_cliente.save()
        messages.success(request, "Cliente agregado exitosamente.")
        return redirect('listado_cliente')

    return render(request, 'Cliente/agregarCliente.html')

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == "POST":
        cliente.cedula = request.POST.get('cedula')
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.telefono = request.POST.get('telefono')
        cliente.email = request.POST.get('email')
        cliente.direccion = request.POST.get('direccion')
        cliente.save()
        messages.success(request, "Cliente editado exitosamente.")
        return redirect('listado_cliente')

    return render(request, 'Cliente/editar_cliente.html', {'cliente': cliente})



def eliminarCliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.delete()
    messages.success(request, "Cliente eliminado exitosamente.")
    return redirect('listado_cliente')



def agregarContratista(request):
    contratista = Contratista.objects.all()  
    return render(request, 'Contratista/agregarContratista.html', { 'contratista': contratista})


def listado_contratista(request):
    contratista = Contratista.objects.all()
    return render(request, 'Contratista/listado_contratista.html', {'contratista': contratista})


def guardarContratista(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        empresa = request.POST.get('empresa')
        foto = request.FILES.get('foto')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')

        nuevo_contratista = Contratista(

            nombre=nombre,
            empresa=empresa,
            foto=foto,
            telefono=telefono,
            email=email,
            direccion=direccion
        )
        nuevo_contratista.save()
        messages.success(request, "Contratista agregado exitosamente.")
        return redirect('listado_contratista')

    return render(request, 'Contratista/agregarContratista.html')

def editar_contratista(request, contratista_id):
    contratista = get_object_or_404(Contratista, id=contratista_id)
    if request.method == "POST":
        contratista.nombre = request.POST.get('nombre')
        contratista.empresa = request.POST.get('empresa')
        
        if 'foto' in request.FILES:
            contratista.foto = request.FILES['foto']

        contratista.telefono = request.POST.get('telefono')
        contratista.email = request.POST.get('email')
        contratista.direccion = request.POST.get('direccion')
        contratista.save()
        messages.success(request, "Contratista editado exitosamente.")
        return redirect('listado_contratista')

    return render(request, 'Contratista/editar_contratista.html', {'contratista': contratista})



def eliminarContratista(request, contratista_id):
    contratista = get_object_or_404(Contratista, id=contratista_id)
    contratista.delete()
    messages.success(request, "Contratista eliminado exitosamente.")
    return redirect('listado_contratista')





def agregarParque(request):
    return render(request, 'ParqueRecreativo/agregarParque.html')

def listado_parques(request):
    parques = ParqueRecreativo.objects.all()
    return render(request, 'ParqueRecreativo/listado_parques.html', {'parques': parques})

def guardarParque(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        ubicacion = request.POST.get('ubicacion')
        area = request.POST.get('area')
        capacidad = request.POST.get('capacidad')
        descripcion = request.POST.get('descripcion')

        nuevo_parque = ParqueRecreativo(
            nombre=nombre,
            ubicacion=ubicacion,
            area=area,
            capacidad=capacidad,
            descripcion=descripcion
        )
        nuevo_parque.save()
        messages.success(request, "Parque agregado exitosamente.")
        return redirect('listado_parques')

    return render(request, 'ParqueRecreativo/agregarParque.html')

def editar_parque(request, parque_id):
    parque = get_object_or_404(ParqueRecreativo, id=parque_id)
    if request.method == "POST":
        parque.nombre = request.POST.get('nombre')
        parque.ubicacion = request.POST.get('ubicacion')
        area_str = request.POST['area'].replace(',', '.')
        parque.area = Decimal(area_str)
        parque.capacidad = request.POST.get('capacidad')
        parque.descripcion = request.POST.get('descripcion')
        parque.save()
        messages.success(request, "Parque editado exitosamente.")
        return redirect('listado_parques')

    return render(request, 'ParqueRecreativo/editar_parque.html', {'parque': parque})

def eliminar_parque(request, parque_id):
    parque = get_object_or_404(ParqueRecreativo, id=parque_id)
    parque.delete()
    messages.success(request, "Parque eliminado exitosamente.")
    return redirect('listado_parques')





def agregar_proyecto(request):
    # Aquí obtienes los parques y contratistas para mostrarlos en el formulario
    parques = ParqueRecreativo.objects.all()
    contratistas = Contratista.objects.all()
 
    return render(request, 'ProyectoConstruccion/agregar_proyecto.html', {
        'parques': parques,
        'contratistas': contratistas
    })

def listado_proyectos(request):
    proyectos = ProyectoConstruccion.objects.all()
    return render(request, 'ProyectoConstruccion/listado_proyectos.html', {'proyectos': proyectos})

def guardar_proyecto(request):
    if request.method == "POST":
        parque_id = request.POST.get('parque')
        contratista_id = request.POST.get('contratista')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        presupuesto = request.POST.get('presupuesto')
        estado = request.POST.get('estado')

        nuevo_proyecto = ProyectoConstruccion(
            parque_id=parque_id,
            contratista_id=contratista_id,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            presupuesto=presupuesto,
            estado=estado
        )
        nuevo_proyecto.save()
        messages.success(request, "Proyecto agregado exitosamente.")
        return redirect('listado_proyectos')

    return render(request, 'ProyectoConstruccion/agregar_proyecto.html')

def editar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(ProyectoConstruccion, id=proyecto_id)
    parques = ParqueRecreativo.objects.all()
    contratistas = Contratista.objects.all()

    if request.method == "POST":
        proyecto.parque_id = request.POST.get('parque')
        proyecto.contratista_id = request.POST.get('contratista')
        proyecto.fecha_inicio = request.POST.get('fecha_inicio')
        proyecto.fecha_fin = request.POST.get('fecha_fin')
        presu_str = request.POST['presupuesto'].replace(',', '.')
        proyecto.presupuesto = Decimal(presu_str)
        proyecto.estado = request.POST.get('estado')
        proyecto.save()
        messages.success(request, "Proyecto editado exitosamente.")
        return redirect('listado_proyectos')

    return render(request, 'ProyectoConstruccion/editar_proyecto.html', {
        'proyecto': proyecto,
        'parques': parques,
        'contratistas': contratistas
    })

def eliminar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(ProyectoConstruccion, id=proyecto_id)
    proyecto.delete()
    messages.success(request, "Proyecto eliminado exitosamente.")
    return redirect('listado_proyectos')
