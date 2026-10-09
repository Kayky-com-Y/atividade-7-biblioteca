from django.contrib import admin
from .models import Livro, Author, Category

# Register your models here.
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano_publicacao', 'disponivel')
    list_filter = ('disponivel', 'category')
    filter_horizontal = ('category', 'autor_many')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)