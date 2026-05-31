from django import forms
from .models import Livro, Emprestimo
import datetime

class FormularioLivro(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'isbn', 'ano_publicacao', 'editora', 'sinopse', 'status', 'categoria']
        widgets = {
            'sinopse': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_ano_publicacao(self):
        ano = self.cleaned_data.get('ano_publicacao')
        ano_atual = datetime.date.today().year
        if ano < 1450 or ano > ano_atual:
            raise forms.ValidationError(f'Ano de publicação deve estar entre 1450 e {ano_atual}.')
        return ano

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn', '').replace('-', '').replace(' ', '')
        if isbn and len(isbn) not in [10, 13]:
            raise forms.ValidationError('ISBN deve ter 10 ou 13 dígitos.')
        return isbn


class FormularioEmprestimo(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['livro', 'data_devolucao_prevista', 'observacoes']
        widgets = {
            'data_devolucao_prevista': forms.DateInput(attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_data_devolucao_prevista(self):
        data = self.cleaned_data.get('data_devolucao_prevista')
        if data and data <= datetime.date.today():
            raise forms.ValidationError('A data de devolução deve ser futura.')
        return data

    def clean_livro(self):
        livro = self.cleaned_data.get('livro')
        if livro and livro.status != 'disponivel':
            raise forms.ValidationError('Este livro não está disponível para empréstimo.')
        return livro
