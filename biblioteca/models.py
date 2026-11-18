from django.core.exceptions import ValidationError
from django.core.validators import (MaxValueValidator, MinLengthValidator, MinValueValidator, RegexValidator,
)
from django.db import models
from django.contrib import admin
from django.utils import timezone


def validar_ano_publicacao(ano):
    if ano > timezone.localdate().year: 
        raise ValidationError('O ano de publicação não pode ser posterior ao ano atual.', code='max_value')

# Create your models here.


class Livro(models.Model):
    titulo = models.CharField(max_length=200, validators=[MinLengthValidator(3, message='O título deve ter pelo menos 3 caracteres.')])
    autor = models.ForeignKey('Author', related_name='books', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ManyToManyField('Category', related_name='category', blank=True, null=True)
    ano_publicacao = models.IntegerField(validators=[MinValueValidator(1450, message='O ano de publicação deve ser 1450 ou posterior.'), validar_ano_publicacao])
    paginas = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1, message='O livro deve ter pelo menos 1 página.'), MaxValueValidator(5000, message='O livro não pode ter mais de 5000 páginas.')])
    isbn = models.CharField(max_length=13, blank=True, validators=[RegexValidator(regex=r'^[0-9]{13}$', message='O ISBN deve conter exatamente 13 dígitos.')])
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

class LivroInline(admin.TabularInline):
    model = Livro
    extra = 2

class Author(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    inlines = [LivroInline]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
