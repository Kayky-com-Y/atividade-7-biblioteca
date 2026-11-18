from datetime import date

from django import forms
from .models import Livro, Author, Category

class AutorForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Nome do autor')
    nationality = forms.CharField(max_length=100, required=False, label='Nacionalidade do autor')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('O autor deve ter um nome.')
        return name

    def clean_nationality(self):
        nationality = self.cleaned_data.get('nationality')
        if nationality and len(nationality) > 50:
            raise forms.ValidationError('A nacionalidade não pode ter mais de 50 caracteres.')
        return nationality

    class Meta:
        model = Author
        fields = ['name', 'nationality']

class LivroForm(forms.ModelForm):
    titulo = forms.CharField(max_length=200, label='Título do livro', error_messages={'required': 'Informe um título com pelo menos 3 caracteres.'},
    )
    autor = forms.ModelChoiceField(queryset=Author.objects.all(), label='Autor')
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False, label='Categorias', widget=forms.CheckboxSelectMultiple,)
    ano_publicacao = forms.IntegerField(label='Ano de publicação')
    disponivel = forms.BooleanField(required=False, label='Disponível')

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        titulo = ' '.join(titulo.split())
        if len(titulo) < 3:
            raise forms.ValidationError(
                'O título deve ter pelo menos 3 caracteres após remover os espaços extras.'
            )
        return titulo

    def clean_ano_publicacao(self):
        ano = self.cleaned_data['ano_publicacao']
        if ano > date.today().year:
            raise forms.ValidationError(
                'O ano de publicação não pode ser futuro. Informe o ano atual ou um ano anterior.'
            )
        return ano

    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'category', 'ano_publicacao', 'disponivel']