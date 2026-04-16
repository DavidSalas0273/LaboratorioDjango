from django.shortcuts import render, redirect
from .models import Asistencia
from .forms import AsistenciaForm


def inicio(request):
    """Página simple de inicio (mantener compatibilidad).
    Redirige a la lista de asistencias.
    """
    return redirect('asistencia:list')


def asistencia_create(request):
    """Vista para crear una Asistencia mediante un formulario.

    GET: muestra el formulario.
    POST: valida y guarda la instancia, luego redirige a la lista.
    """
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asistencia:list')
    else:
        form = AsistenciaForm()
    return render(request, 'asistencia/asistencia_form.html', {'form': form})


def asistencia_list(request):
    """Lista las asistencias registradas."""
    items = Asistencia.objects.all().order_by('-fecha', '-hora_ingreso')
    return render(request, 'asistencia/asistencia_list.html', {'items': items})