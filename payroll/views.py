from django.shortcuts import render, redirect
from .models import Empleado
from .forms import EmpleadoForm
#from django.http import HttpResponse
# Create your views here.

def login(request):
    return render(request, 'registration/login.html')

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def empleados(request):
    empleados = Empleado.objects.all()
    return render(request,'empleados/index.html',{'empleados':empleados})

def crear_empleado(request):
    formulario = EmpleadoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('empleados')
    return render(request, 'empleados/crear.html', {'formulario':formulario})

def editar_empleado(request,id):
    empleado = Empleado.objects.get(id=id)
    formulario = EmpleadoForm(request.POST or None, request.FILES or None, instance=empleado) 
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('empleados')
    return render(request, 'empleados/editar.html', {'formulario':formulario})

def eliminar(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect('empleados')