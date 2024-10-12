from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def lista_empleados(request):
    # Lista de nombres de empleados
    empleados = ['Juan Pérez', 'Ana González', 'Carlos Rojas', 'Marta López', 'Luis Ramírez']
    
    # Pasamos la lista de empleados al contexto
    context = {
        'empleados': empleados
    }
    
    return render(request, 'empleados.html', context)
