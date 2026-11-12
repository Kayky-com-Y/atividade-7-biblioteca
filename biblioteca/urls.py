from .views import lista_livros, author_detail, author_create, lista_autores
from django.urls import path
urlpatterns = [
    path('livros/', lista_livros, name='lista_livros'),
    path('', lista_autores, name='lista_autores'),
    path('author/<int:author_id>/', author_detail, name='author_detail'),
    path('author/create/', author_create, name='author_create'),
]