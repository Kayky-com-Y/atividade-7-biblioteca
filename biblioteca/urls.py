from django.urls import path

from .views import (author_create, author_detail, lista_autores, lista_livros, livro_create, livro_delete, livro_detail, livro_update, sobre)

urlpatterns = [
    path('livros/', lista_livros.as_view(), name='lista_livros'),
    path('', lista_autores.as_view(), name='lista_autores'),
    path('author/<int:author_id>/', author_detail.as_view(), name='author_detail'),
    path('author/create/', author_create.as_view(), name='author_create'),
    path('livro/create/', livro_create.as_view(), name='livro_create'),
    path('livro/<int:livro_id>/', livro_detail.as_view(), name='livro_detail'),
    path('livro/<int:livro_id>/update/', livro_update.as_view(), name='livro_update'),
    path('livro/<int:livro_id>/delete/', livro_delete.as_view(), name='livro_delete'),
    path('sobre/', sobre.as_view(), name='sobre'),
]