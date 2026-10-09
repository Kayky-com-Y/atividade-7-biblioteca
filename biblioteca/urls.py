from .views import lista_livros
from django.urls import path
urlpatterns = [
    path('livros/', lista_livros, name='lista_livros'),
]