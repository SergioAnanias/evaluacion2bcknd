from django.shortcuts import render,redirect
from app.models import *
from django.contrib import messages
# Create your views here.
def index(request):
    if len(Estados.objects.filter()) == 0:
        Estados.objects.create(
            desc_estado='Reservada'
        )
        Estados.objects.create(
            desc_estado='Completada'
        )
        Estados.objects.create(
            desc_estado='Anulada'
        )
        Estados.objects.create(
            desc_estado='No asiste'
        )
    context = {
        'data': Reserva.objects.all()
    }
    return render(request, 'index.html',context)

def register_reserva(request):
    estados=Estados.objects.all()
    return render(request, 'register_reserva.html', context={'estados':estados})


def create(request):
    errors = Reserva.objects.validator(request.POST)
# En caso de que se devuelvan errores del validador, se guardan con messages y se redirecciona al formulario de registro para mostrarlos
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect("/register_reserva")

    nuevaReserva= Reserva.objects.create(
        rut=request.POST['rut'],
        nombre=request.POST['nombre'],
        telefono=request.POST['telefono'],
        fecha=request.POST['fecha'],
        hora=request.POST['hora'],
        personas=request.POST['personas'],
        observacion=request.POST['observacion']

    )
    return redirect("/")


def edit(request, id_reserva):
    reserva = Reserva.objects.get(id=id_reserva)
    context = {
        'reserva':reserva,
        'estados':Estados.objects.all()
    }
    return render(request, "edit.html", context)

def update(request, id_reserva):
    errors = Reserva.objects.validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect("/editar_reserva/"+id_reserva)

    reserva = Reserva.objects.filter(id=id_reserva)
    reserva.update(
        rut=request.POST['rut'],
        nombre=request.POST['nombre'],
        telefono=request.POST['telefono'],
        fecha=request.POST['fecha'],
        hora=request.POST['hora'],
        personas=request.POST['personas'],
        estado= request.POST['estado'],
        observacion=request.POST['observacion']
    )
    return redirect("/")

def delete(request,id_reserva):
    reserva = Reserva.objects.filter(id=id_reserva).delete()
    return redirect("/")