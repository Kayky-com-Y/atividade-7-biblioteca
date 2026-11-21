from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Livro, Author, Category
from .forms import LivroForm, AutorForm


class LivroListView(ListView):
    model = Livro
    template_name = 'lista_livros.html'
    context_object_name = 'livros'
    ordering = ['titulo']


class LivroDetailView(DetailView):
    model = Livro
    template_name = 'livro_detail.html'
    context_object_name = 'livro'


class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'livro_form.html'
    success_url = reverse_lazy('lista_livros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Novo livro'
        context['botao'] = 'Cadastrar livro'
        return context


class LivroUpdateView(UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = 'livro_form.html'
    context_object_name = 'livro'
    success_url = reverse_lazy('lista_livros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar livro'
        context['botao'] = 'Salvar alterações'
        return context


class LivroDeleteView(DeleteView):
    model = Livro
    template_name = 'livro_confirm_delete.html'
    success_url = reverse_lazy('lista_livros')


class SobreView(TemplateView):
    template_name = 'sobre.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_livros'] = Livro.objects.count()
        context['livros_disponiveis'] = Livro.objects.filter(disponivel=True).count()
        return context


# Mantenha as views de Author que ainda não foram refatoradas
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