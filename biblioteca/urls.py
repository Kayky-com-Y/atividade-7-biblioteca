from django.urls import path
from .views import (
    LivroListView, LivroDetailView, LivroCreateView, LivroUpdateView, LivroDeleteView,
    SobreView, author_detail, view_author_form, lista_authors
)

urlpatterns = [
    path('', LivroListView.as_view(), name='lista_livros'),
    path('livro/<int:pk>/', LivroDetailView.as_view(), name='livro_detail'),
    path('livro/novo/', LivroCreateView.as_view(), name='livro_form'),
    path('livro/<int:pk>/editar/', LivroUpdateView.as_view(), name='edit_livro'),
    path('livro/<int:pk>/excluir/', LivroDeleteView.as_view(), name='delete_livro'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    
    path('author/<int:author_id>/', author_detail, name='author_detail'),
    path('author/form/', view_author_form, name='author_form'),
    path('authors/', lista_authors, name='lista_authors'),
]