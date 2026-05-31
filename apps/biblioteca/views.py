from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
import datetime
from .models import Livro, Categoria, Emprestimo
from .forms import FormularioLivro, FormularioEmprestimo


def lista_livros(request):
    livros = Livro.objects.select_related('categoria', 'cadastrado_por').all()
    query = request.GET.get('q', '')
    categoria_id = request.GET.get('categoria', '')
    status = request.GET.get('status', '')

    if query:
        livros = livros.filter(
            Q(titulo__icontains=query) |
            Q(autor__icontains=query) |
            Q(isbn__icontains=query)
        )
    if categoria_id:
        livros = livros.filter(categoria_id=categoria_id)
    if status:
        livros = livros.filter(status=status)

    categorias = Categoria.objects.all()
    return render(request, 'biblioteca/lista_livros.html', {
        'livros': livros,
        'categorias': categorias,
        'query': query,
        'categoria_id': categoria_id,
        'status': status,
    })


def detalhe_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    emprestimos = livro.emprestimos.select_related('usuario').all()
    return render(request, 'biblioteca/detalhe_livro.html', {
        'livro': livro,
        'emprestimos': emprestimos,
    })


@login_required
def criar_livro(request):
    if request.method == 'POST':
        form = FormularioLivro(request.POST)
        if form.is_valid():
            livro = form.save(commit=False)
            livro.cadastrado_por = request.user
            livro.save()
            messages.success(request, f'Livro "{livro.titulo}" cadastrado com sucesso!')
            return redirect('biblioteca:detalhe_livro', pk=livro.pk)
    else:
        form = FormularioLivro()
    return render(request, 'biblioteca/form_livro.html', {'form': form, 'titulo': 'Cadastrar Livro'})


@login_required
def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if livro.cadastrado_por != request.user:
        messages.error(request, 'Você não tem permissão para editar este livro.')
        return redirect('biblioteca:detalhe_livro', pk=pk)
    if request.method == 'POST':
        form = FormularioLivro(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            messages.success(request, f'Livro "{livro.titulo}" atualizado com sucesso!')
            return redirect('biblioteca:detalhe_livro', pk=pk)
    else:
        form = FormularioLivro(instance=livro)
    return render(request, 'biblioteca/form_livro.html', {'form': form, 'titulo': 'Editar Livro', 'livro': livro})


@login_required
def excluir_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if livro.cadastrado_por != request.user:
        messages.error(request, 'Você não tem permissão para excluir este livro.')
        return redirect('biblioteca:detalhe_livro', pk=pk)
    if request.method == 'POST':
        titulo = livro.titulo
        livro.delete()
        messages.success(request, f'Livro "{titulo}" excluído com sucesso!')
        return redirect('biblioteca:lista_livros')
    return render(request, 'biblioteca/confirmar_exclusao.html', {'livro': livro})


@login_required
def meus_emprestimos(request):
    emprestimos = Emprestimo.objects.filter(usuario=request.user).select_related('livro')
    return render(request, 'biblioteca/meus_emprestimos.html', {'emprestimos': emprestimos})


@login_required
def criar_emprestimo(request):
    if request.method == 'POST':
        form = FormularioEmprestimo(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            emprestimo.usuario = request.user
            emprestimo.save()
            emprestimo.livro.status = 'emprestado'
            emprestimo.livro.save()
            messages.success(request, f'Empréstimo de "{emprestimo.livro.titulo}" registrado!')
            return redirect('biblioteca:meus_emprestimos')
    else:
        form = FormularioEmprestimo()
    return render(request, 'biblioteca/form_emprestimo.html', {'form': form})


@login_required
def devolver_livro(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk, usuario=request.user)
    if request.method == 'POST':
        emprestimo.data_devolucao_real = datetime.date.today()
        emprestimo.status = 'devolvido'
        emprestimo.save()
        emprestimo.livro.status = 'disponivel'
        emprestimo.livro.save()
        messages.success(request, f'Livro "{emprestimo.livro.titulo}" devolvido com sucesso!')
        return redirect('biblioteca:meus_emprestimos')
    return render(request, 'biblioteca/confirmar_devolucao.html', {'emprestimo': emprestimo})
