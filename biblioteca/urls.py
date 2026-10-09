from .views import lista_livros, author_detail
from django.urls import path
urlpatterns = [
    path('livros/', lista_livros, name='lista_livros'),
    path('author/<int:author_id>/', author_detail, name='author_detail')
]