from .views import (author_create, author_detail, livro_detail, livro_form, lista_autores, lista_livros,)
from django.urls import path
urlpatterns = [
    path('livros/', lista_livros, name='lista_livros'),
    path('', lista_autores, name='lista_autores'),
    path('author/<int:author_id>/', author_detail, name='author_detail'),
    path('author/create/', author_create, name='author_create'),
    path('livro/create/', livro_form, name='livro_create'),
    path('livro/<int:livro_id>/', livro_detail, name='livro_detail'),
    path('livro/<int:livro_id>/update/', livro_form, name='livro_update'),
]