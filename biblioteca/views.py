from django.shortcuts import render
from .models import Livro
# Create your views here.

def lista_livros(request):
    livros = Livro.objects.all()
    context = {
        'livros': livros
    }
    return render(request, 'lista_livros.html', context)
