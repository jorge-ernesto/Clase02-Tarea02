from django.shortcuts import render, redirect
from .forms import AlumnoForm
from .models import Alumno
from datetime import datetime

# Create your views here.

def alumno_list(request):
    context = {'alumno_list': Alumno.objects.all()}
    return render(request, "app/alumno_list.html", context)

def alumno_form(request, id = 0): # id por defecto es 0
    if request.method == "GET": # Metodo GET. "http://127.0.0.1:8000/alumnos" o "http://127.0.0.1:8000/alumnos/1".
        if id == 0: # Vista por defecto, formulario vacio
            form = AlumnoForm()
        else: # Vista con datos, formulario con datos del alumno elegido
            alumno = Alumno.objects.get(pk = id)
            alumno = convertir_fecha(alumno)
            form = AlumnoForm(instance = alumno)

        return render(request, "app/alumno_form.html", {'form': form})

    else: # Metodo POST
        # Crear una copia mutable de request.POST
        post_data = request.POST.copy()
        # Modificar la copia mutable de request.POST
        post_data['edad'] = obtener_edad(request)

        if id == 0: # Guardar alumno
            form = AlumnoForm(post_data)
        else:  # Editar alumno
            alumno = Alumno.objects.get(pk = id)
            form = AlumnoForm(post_data, instance = alumno)

        # Guardar o editar
        if form.is_valid():
            form.save()

        return redirect('/alumnos/list')

def convertir_fecha(alumno):
    print('fecha_nacimiento', type(alumno.fecha_nacimiento), alumno.fecha_nacimiento)
    # Modificar el formato de fecha a 'yyyy-mm-dd'
    fecha_nacimiento = alumno.fecha_nacimiento
    alumno.fecha_nacimiento = fecha_nacimiento.strftime('%Y-%m-%d')
    # Cerrar
    print('fecha_nacimiento', type(alumno.fecha_nacimiento), alumno.fecha_nacimiento)
    return alumno

def obtener_edad(request):
    fecha_nacimiento_str = request.POST['fecha_nacimiento'] # Obtener fecha de nacimiento en formato texto
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d') # Convertir a objeto datetime
    hoy = datetime.now()  # Obtener fecha actual
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day)) # Obtener edad
    return edad

def alumno_delete(request, id):
    alumno = Alumno.objects.get(pk = id)
    alumno.delete()
    return redirect('/alumnos/list')
