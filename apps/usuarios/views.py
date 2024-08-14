from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages 

def login(request):
    form1 = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome=form['nomelogin'].value()
            senha1=form['senha'].value()

        usuario = auth.authenticate(
            request,
            username = nome,
            password = senha1,
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, 'Usuário logado com sucesso')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')
            

    return render(request, 'usuarios/login.html', {'form': form1})



def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            nome=form['nomecadastro'].value()
            email=form['emailcadastro'].value()
            senha1=form['senha1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário ja existente')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha1         
            )
            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso')
            return redirect('login')
    return render(request, 'usuarios/cadastro.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'logout efetuado com sucesso')
    return redirect('login')


