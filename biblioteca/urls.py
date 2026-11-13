from .views import lista_livros, author_detail, view_author_form, lista_authors, livro_form
from django.urls import path
urlpatterns = [
    path('', lista_livros, name='lista_livros'),
    path('author/<int:author_id>/', author_detail, name='author_detail'),
    path('author/form/', view_author_form, name='author_form'),
    path('authors/', lista_authors, name='lista_authors'),
    path('livro/form/', livro_form, name='livro_form'),
    path('livro/form/<int:livro_id>/', livro_form, name='edit_livro'),
]