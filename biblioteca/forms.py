from django.utils import timezone
from django import forms
from .models import Livro


class AutorForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nome do Autor')
    nationality = forms.CharField(max_length=50, required=False, label='Nacionalidade')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('O nome do autor é obrigatório.')
        return name
    
    def clean_nationality(self):
        nationality = self.cleaned_data.get('nationality')
        if nationality and len(nationality) > 50:
            raise forms.ValidationError('A nacionalidade não pode ter mais de 50 caracteres.')
        return nationality


class LivroForm(forms.ModelForm):

    class Meta:
        model = Livro
        fields = [
            'titulo',
            'autor_many',
            'ano_publicacao',
            'paginas',  
            'isbn',     
            'disponivel',
            'category'
        ]

        labels = {
            'titulo': 'Título',
            'autor_many': 'Autor(es)',
            'ano_publicacao': 'Ano de publicação',
            'paginas': 'Número de Páginas',
            'isbn': 'ISBN',
            'disponivel': 'Disponível',
            'category': 'Categorias'
        }

        widgets = {
            'autor_many': forms.SelectMultiple(),
            'category': forms.CheckboxSelectMultiple()
        }
