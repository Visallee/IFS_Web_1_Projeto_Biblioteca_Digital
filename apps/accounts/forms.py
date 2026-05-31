from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class FormularioCadastro(UserCreationForm):
    email = forms.EmailField(required=True, label='E-mail')
    first_name = forms.CharField(max_length=100, required=True, label='Nome')
    last_name = forms.CharField(max_length=100, required=True, label='Sobrenome')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está em uso.')
        return email

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.email = self.cleaned_data['email']
        if commit:
            usuario.save()
            Perfil.objects.create(usuario=usuario)
        return usuario


class FormularioPerfil(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=True, label='Nome')
    last_name = forms.CharField(max_length=100, required=True, label='Sobrenome')
    email = forms.EmailField(required=True, label='E-mail')

    class Meta:
        model = Perfil
        fields = ['bio', 'data_nascimento']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'bio': forms.Textarea(attrs={'rows': 3}),
        }
