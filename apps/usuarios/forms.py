from typing import Any
from django import forms

class LoginForms(forms.Form):
    nomelogin = forms.CharField(
        label='Nome de login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva'
            }
        ),
    )

    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=60,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Digite sua senha'
            }
        ),
    )




class CadastroForms(forms.Form):
    nomecadastro = forms.CharField(
        label='Nome completo',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Joao Silva'
            }
        ),
    )

    emailcadastro = forms.EmailField(
        label='Email',
        required=True,
        max_length=40,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com'
            }
        ),
    )

    senha1=forms.CharField(
    label='Senha',
    required=True,
    max_length=60,
    widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ex.: Digite sua senha'
            }
        ),
    )
    senha2=forms.CharField(
    label='Confirme sua senha',
    required=True,
    max_length=60,
    widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ex.: Digite sua senha mais uma vez'
            }
        ),
    )
    
    def clean_nomecadastro(self):
        nome = self.cleaned_data.get('nomecadastro')
        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError("Não é possivel inserir espaços dentro do campo usuário")
            else:
                return nome
    

    def clean_senha2(self):
        senha1 = self.cleaned_data.get('senha1')
        senha2 = self.cleaned_data.get('senha2')

        if senha1 and senha2:
            if senha1 != senha2:
                raise forms.ValidationError('As senhas não coincidem')
        else:
            return senha2