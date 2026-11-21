from django.db import models
from django.contrib import admin
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator, RegexValidator, FileExtensionValidator
from .validators import validar_ano_publicacao, validar_tamanho_arquivo

class Livro(models.Model):
    titulo = models.CharField(max_length=200, validators=[MinLengthValidator(3, message='O título deve ter no mínimo 3 caracteres.')])
    autor_many = models.ManyToManyField('Author', related_name='books', blank=True)
    category = models.ManyToManyField('Category', related_name='books', blank=True, null=True)
    ano_publicacao = models.IntegerField(validators=[validar_ano_publicacao])
    paginas = models.IntegerField(blank=True, null=True, verbose_name='Páginas', validators=[
            MinValueValidator(1, message='O livro deve ter pelo menos 1 página.'),
            MaxValueValidator(5000, message='O limite é de 5000 páginas.')])
    isbn = models.CharField(max_length=13, blank=True, null=True, verbose_name='ISBN', validators=[RegexValidator(r'^\d{13}$', message='O ISBN deve ter exatamente 13 dígitos numéricos.')])
    disponivel = models.BooleanField(default=True)

    capa = models.ImageField(upload_to='capas/', blank=True, null=True, verbose_name='Capa do Livro', validators=[validar_tamanho_arquivo, FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])

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
