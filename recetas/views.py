from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Receta
from .forms import RecetaForm

def lista_recetas(request):
    query = request.GET.get('q')
    if query:
        recetas = Receta.objects.filter(Q(titulo__icontains=query) | Q(descripcion__icontains=query))
    else:
        recetas = Receta.objects.all()
    return render(request, 'recetas/lista.html', {'recetas': recetas})

@login_required
def crear_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            receta = form.save(commit=False)
            receta.autor = request.user
            receta.save()
            return redirect('lista_recetas')
    else:
        form = RecetaForm()
    return render(request, 'recetas/form_receta.html', {'form': form})

# VISTA 3: Ver el detalle de una sola receta
def detalle_receta(request, id):
    receta = get_object_or_404(Receta, id=id)
    return render(request, 'recetas/detalle.html', {'receta': receta})

# VISTA 4: Editar Receta
@login_required
def editar_receta(request, id):
    receta = get_object_or_404(Receta, id=id)
    
    # Seguridad: Si el usuario NO es el dueño, lo sacamos de aquí
    if request.user != receta.autor:
        return redirect('lista_recetas')

    if request.method == 'POST':
        # "instance=receta" es la clave: le dice a Django que NO cree una nueva, sino que actualice esta
        form = RecetaForm(request.POST, request.FILES, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('detalle_receta', id=id) # Te devuelve al detalle actualizado
    else:
        # Cargamos el formulario con los datos actuales de la receta
        form = RecetaForm(instance=receta)

    return render(request, 'recetas/form_receta.html', {'form': form})