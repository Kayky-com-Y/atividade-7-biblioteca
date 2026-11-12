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