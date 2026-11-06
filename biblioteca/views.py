from django.shortcuts import render, redirect
from .models import Livro, Author, Category
from django.shortcuts import get_object_or_404
from .forms import AutorForm

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

def view_author_form(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            nationality = form.cleaned_data['nationality']
            author = Author(name=name, nationality=nationality)
            author.save() 

        return redirect('author_detail', author_id=author.id)
    else:

        form = AutorForm()
    return render(request, 'author_form.html', {'form': form})

def lista_authors(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'lista_authors.html', context)