from django.shortcuts import render, redirect, get_object_or_404
from .models import Carros
from .forms import ModelForm, CarrosForm


def lista_carros(request):
    context = {
        'carros': Carros.objects.all()
    }
    return render(request, 'carros.html', context)


def novos_carros(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_carros')
    return render(request, 'carros_novos.html', {'form': form})


def alterar_carros(request, id):
    carro = get_object_or_404(Carros, pk=id)
    form = CarrosForm(request.POST or None, instance=carro)
    if form.is_valid():
        form.save()
        return redirect('lista_carros')
    return render(request, 'carros_novos.html', {'form': form})


def deletar_carros(request, id):
    carro = get_object_or_404(Carros, pk=id)
    form = CarrosForm(request.POST or None, instance=carro)
    if request.method == 'POST':
        carro.delete()
        return redirect('lista_carros')
    return render(request, 'deletar_carros.html', {'form': form})
