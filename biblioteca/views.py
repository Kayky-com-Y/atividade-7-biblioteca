from django.shortcuts import render
from .models import Livro, Author, Category
from django.shortcuts import get_object_or_404
# Create your views here.

def lista_livros(request):
    livros = Livro.objects.all()
    context = {
        'livros': livros
    }
    return render(request, 'lista_livros.html', context)

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    livros = Livro.objects.filter(autor_many=author)
    context = {
        'author': author,
        'livros': livros
    }
    return render(request, 'author_detail.html', context)