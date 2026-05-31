from django.contrib import admin
from .models import Livro, Categoria, Emprestimo

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'categoria', 'status', 'cadastrado_por']
    list_filter = ['status', 'categoria']
    search_fields = ['titulo', 'autor', 'isbn']

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ['livro', 'usuario', 'data_emprestimo', 'data_devolucao_prevista', 'status']
    list_filter = ['status']
