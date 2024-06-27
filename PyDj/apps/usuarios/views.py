from django.shortcuts import render,redirect
from apps.usuarios.forms import LoginForms,CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth,messages

#MESSAGES CORRIGIR
def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha_login"].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
            if usuario != None:
                auth.login(request,usuario)
                return redirect('index')
            else:
                messages.error(request,"Usuario ou senha incorretos")
                return redirect('login')

    return render(request, "usuarios/login.html", {"form":form})

def cadastro(request):
    form = CadastroForms()

    if request.method =='POST':
        form = CadastroForms(request.POST)

        if form.is_valid():


            nome=form["nome_cadastro"].value()
            email=form["email_cadastro"].value()
            senha1=form["senha_login1"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuario já existente")
                return redirect('cadastro')

            usuario=User.objects.create_user(
                username=nome,
                email=email,
                password=senha1
            )
            usuario.save()
            messages.success(request,"Usuario Cadastrado com sucesso")
            return redirect('login')

    return render(request, "usuarios/cadastro.html",{"form":form})

def logout(request):
    auth.logout(request)
    messages.success(request,"Logout efetuado com sucesso")
    return redirect('login')
