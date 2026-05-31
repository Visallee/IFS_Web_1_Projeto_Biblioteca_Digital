from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import FormularioCadastro, FormularioPerfil
from .models import Perfil

def cadastro(request):
    if request.user.is_authenticated:
        return redirect('biblioteca:lista_livros')
    if request.method == 'POST':
        form = FormularioCadastro(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, f'Bem-vindo(a), {usuario.first_name}! Conta criada com sucesso.')
            return redirect('biblioteca:lista_livros')
    else:
        form = FormularioCadastro()
    return render(request, 'accounts/cadastro.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('biblioteca:lista_livros')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, f'Olá, {usuario.first_name or usuario.username}! Login realizado com sucesso.')
            return redirect(request.GET.get('next', 'biblioteca:lista_livros'))
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'Você saiu da sua conta.')
    return redirect('accounts:login')


@login_required
def perfil(request):
    perfil_obj, _ = Perfil.objects.get_or_create(usuario=request.user)
    if request.method == 'POST':
        form = FormularioPerfil(request.POST, instance=perfil_obj)
        if form.is_valid():
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            request.user.save()
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('accounts:perfil')
    else:
        form = FormularioPerfil(instance=perfil_obj, initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        })
    return render(request, 'accounts/perfil.html', {'form': form})
