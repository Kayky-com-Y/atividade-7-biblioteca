from django.db import models
from django.contrib import admin

# Create your models here.


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Author', related_name='books', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ManyToManyField('Category', related_name='books', blank=True, null=True)
    ano_publicacao = models.IntegerField()
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
