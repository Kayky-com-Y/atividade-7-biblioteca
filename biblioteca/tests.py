from datetime import date

from django import forms
from django.test import TestCase
from django.urls import resolve, reverse

from .forms import LivroForm
from .models import Author, Category, Livro
from .views import livro_form


class LivroFormTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Autora')
        self.category = Category.objects.create(name='Ficção')

    def form_data(self, **overrides):
        data = {
            'titulo': 'Livro válido',
            'autor': self.author.pk,
            'ano_publicacao': date.today().year,
            'disponivel': 'on',
        }
        data.update(overrides)
        return data

    def test_title_whitespace_is_normalized_before_saving(self):
        form = LivroForm(self.form_data(titulo='  Meu   livro  '))

        self.assertTrue(form.is_valid(), form.errors)
        livro = form.save()

        self.assertEqual(livro.titulo, 'Meu livro')

    def test_title_must_have_at_least_three_characters_after_normalization(self):
        form = LivroForm(self.form_data(titulo='  a   '))

        self.assertFalse(form.is_valid())
        self.assertIn('título', form.errors['titulo'][0])

    def test_future_publication_year_is_rejected(self):
        form = LivroForm(self.form_data(ano_publicacao=date.today().year + 1))

        self.assertFalse(form.is_valid())
        self.assertIn('futuro', form.errors['ano_publicacao'][0])

    def test_categories_are_optional_checkboxes(self):
        form = LivroForm(self.form_data())

        self.assertFalse(form.fields['category'].required)
        self.assertIsInstance(form.fields['category'].widget, forms.CheckboxSelectMultiple)
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.save().category.count(), 0)

    def test_selected_category_is_saved(self):
        form = LivroForm(self.form_data(category=[self.category.pk]))

        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(list(form.save().category.all()), [self.category])

    def test_create_and_update_routes_share_the_form_view(self):
        self.assertIs(
            resolve(reverse('livro_create')).func,
            livro_form,
        )
        self.assertIs(
            resolve(reverse('livro_update', args=[1])).func,
            livro_form,
        )

    def test_editing_missing_book_returns_404(self):
        response = self.client.get(reverse('livro_update', args=[999]))

        self.assertEqual(response.status_code, 404)

    def test_form_heading_changes_between_create_and_edit(self):
        create_response = self.client.get(reverse('livro_create'))
        livro = Livro.objects.create(
            titulo='Livro existente',
            autor=self.author,
            ano_publicacao=2020,
        )
        edit_response = self.client.get(reverse('livro_update', args=[livro.pk]))

        self.assertContains(create_response, '<h1>Novo livro</h1>', html=True)
        self.assertContains(edit_response, '<h1>Editar livro</h1>', html=True)
