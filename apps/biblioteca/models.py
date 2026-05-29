from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='livros')

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True)
    ano_publicacao = models.IntegerField()
    quantidade_disponivel = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"