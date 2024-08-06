from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms


def login(request):
    form1 = LoginForms()
    return render(request, 'usuarios/login.html', {'form': form1})
def cadastro(request):
    form2 = CadastroForms()
    return render(request, 'usuarios/cadastro.html', {'form': form2})