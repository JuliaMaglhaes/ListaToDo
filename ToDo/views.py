from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import Lista


def index(request):
    lista = Lista.objects.all()
    template_name = 'index.html'
    form = ListaForm()

    if request.method == 'POST':
        form = ListaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context ={
        'lista': lista,
        'form': form,
    }

    return render(request, template_name, context)

def listaf(request, pk):
    lista = Lista.objects.get(pk=pk)
    template_name='listaf.html'
    form = ListaForm(instance= lista)

    if request.method == 'POST':
        form = ListaForm(request.POST, instance= lista)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }

    return render (request, template_name, context)

def deletar(request, pk):
    lista= Lista.objects.get(pk=pk)
    lista.delete()
    return redirect ('index')