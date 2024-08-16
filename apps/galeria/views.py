from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça login para acessar esta página')
        return redirect('login')
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotografias})


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})


def buscar(request,):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça login para acessar esta página')
        return redirect('login')
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    if 'buscar' in request.GET:
        nome_buscar = request.GET['buscar']
        if nome_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_buscar)

    return render(request, 'galeria/index.html', {'cards': fotografias})


def novafotografia(request,):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça login para acessar esta página')
        return redirect('login')
    fotoform = FotografiaForms
    if request.method == 'POST':
        fotoform = FotografiaForms(request.POST, request.FILES)
        if fotoform.is_valid():
            fotoform.save()
            messages.success(request, 'Fotografia adicionada')
            redirect('index')
    return render(request, 'galeria/novafotografia.html', {'form': fotoform})


def editfotografia(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso')
            redirect('index')
    return render(request, 'galeria/editfotografia.html', {'form': form, 'foto_id': foto_id})


def delfotografia(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Deleção feita com sucesso')
    return redirect('index')


def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True, categoria=categoria)

    return render(request, 'galeria/index.html', {'cards': fotografias})