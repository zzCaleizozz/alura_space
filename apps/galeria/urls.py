from django.urls import path

from apps.galeria.views import \
    index, imagem, buscar, novafotografia, delfotografia, editfotografia, filtro
urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('nova-fotografia', novafotografia, name='novafotografia'),
    path('deletar-fotografia/<int:foto_id>', delfotografia, name='delfotografia'),
    path('editar-fotografia/<int:foto_id>', editfotografia, name='editfotografia'),
    path('filtro/<str:categoria>', filtro, name='filtro')
]