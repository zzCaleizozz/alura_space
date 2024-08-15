from django.urls import path

from apps.galeria.views import \
    index, imagem, buscar, novafotografia, delfotografia, editfotografia
urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('nova-fotografia', novafotografia, name='novafotografia'),
    path('deletar-fotografia', delfotografia, name='delfotografia'),
    path('editar-fotografia', editfotografia, name='editfotografia'),
]