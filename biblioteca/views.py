from django.shortcuts import render, redirect
from .models import Livro, Author, Category
from django.shortcuts import get_object_or_404
from .forms import AutorForm, LivroForm
# Create your views here.

def lista_livros(request):
    livros = Livro.objects.all()
    context = {
        'livros': livros
    }
    return render(request, 'lista_livros.html', context)

def lista_autores(request):
    autores = Author.objects.all()
    context = {
        'autores': autores
    }
    return render(request, 'lista_autores.html', context)

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    livros = Livro.objects.filter(autor=author)
    context = {
        'author': author,
        'livros': livros
    }
    return render(request, 'author_detail.html', context)

def author_create(request):
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

def livro_form(request, livro_id=None):
    livro = get_object_or_404(Livro, id=livro_id) if livro_id is not None else None
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            livro = form.save()
            return redirect('author_detail', author_id=livro.autor.id)
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livro_form.html', {'form': form})

def livro_detail(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    context = {
        'livro': livro
    }
    return render(request, 'livro_detail.html', context)