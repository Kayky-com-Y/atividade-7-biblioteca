from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView)

from .forms import AutorForm, LivroForm
from .models import Author, Livro


class lista_livros(ListView):
    model = Livro
    template_name = 'lista_livros.html'
    context_object_name = 'livros'
    queryset = Livro.objects.order_by('titulo')


class lista_autores(ListView):
    model = Author
    template_name = 'lista_autores.html'
    context_object_name = 'autores'


class author_detail(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'
    pk_url_kwarg = 'author_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['livros'] = Livro.objects.filter(autor=self.object)
        return context


class author_create(CreateView):
    model = Author
    form_class = AutorForm
    template_name = 'author_form.html'

    def get_success_url(self):
        return reverse_lazy('author_detail', kwargs={'author_id': self.object.pk})


class livro_success_url_mixin:
    def get_success_url(self):
        return reverse_lazy(
            'author_detail',
            kwargs={'author_id': self.object.autor_id},
        )


class livro_create(livro_success_url_mixin, CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'livro_form.html'


class livro_update(livro_success_url_mixin, UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = 'livro_form.html'
    pk_url_kwarg = 'livro_id'


class livro_detail(DetailView):
    model = Livro
    template_name = 'livro_detail.html'
    context_object_name = 'livro'
    pk_url_kwarg = 'livro_id'


class livro_delete(DeleteView):
    model = Livro
    template_name = 'livro_confirm_delete.html'
    context_object_name = 'livro'
    pk_url_kwarg = 'livro_id'
    success_url = reverse_lazy('lista_livros')


class sobre(TemplateView):
    template_name = 'sobre.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_livros'] = Livro.objects.count()
        context['livros_disponiveis'] = Livro.objects.filter(disponivel=True).count()
        return context
