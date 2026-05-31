from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', blank=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Livro(models.Model):
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('emprestado', 'Emprestado'),
        ('reservado', 'Reservado'),
    ]

    titulo = models.CharField('Título', max_length=200)
    autor = models.CharField('Autor', max_length=200)
    isbn = models.CharField('ISBN', max_length=20, blank=True)
    ano_publicacao = models.IntegerField('Ano de Publicação')
    editora = models.CharField('Editora', max_length=100, blank=True)
    sinopse = models.TextField('Sinopse', blank=True)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='disponivel')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='livros', verbose_name='Categoria')
    cadastrado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='livros_cadastrados', verbose_name='Cadastrado por', default=1)
    data_cadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['titulo']

    def __str__(self):
        return f'{self.titulo} — {self.autor}'


class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('devolvido', 'Devolvido'),
        ('atrasado', 'Atrasado'),
    ]

    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='emprestimos', verbose_name='Livro')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emprestimos', verbose_name='Usuário')
    data_emprestimo = models.DateField('Data do Empréstimo', auto_now_add=True)
    data_devolucao_prevista = models.DateField('Devolução Prevista')
    data_devolucao_real = models.DateField('Devolução Real', null=True, blank=True)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='ativo')
    observacoes = models.TextField('Observações', blank=True)

    class Meta:
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'
        ordering = ['-data_emprestimo']

    def __str__(self):
        return f'{self.livro.titulo} → {self.usuario.username}'
