from django.urls import path
from . import views

app_name = 'biblioteca'  # ← namespace

urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),
    path('livro/<int:pk>/', views.detalhe_livro, name='detalhe_livro'),
    path('livro/novo/', views.criar_livro, name='criar_livro'),
    path('livro/<int:pk>/editar/', views.editar_livro, name='editar_livro'),
    path('livro/<int:pk>/excluir/', views.excluir_livro, name='excluir_livro'),
    path('emprestimos/', views.meus_emprestimos, name='meus_emprestimos'),
    path('emprestimos/novo/', views.criar_emprestimo, name='criar_emprestimo'),
    path('emprestimos/<int:pk>/devolver/', views.devolver_livro, name='devolver_livro'),
]