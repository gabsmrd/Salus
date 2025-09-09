from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants

def cadastro(request):
    if request.user.is_authenticated:
        # Se o usuário já estiver autenticado, redireciona para a página inicial
        return redirect('home')
    
    if request.method == "GET":
        return render(request, 'cadastro.html')
    
    # Quando o formulário for enviado via POST
    else:
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # Verifica se as senhas são iguais
        if senha != confirmar_senha:
            # Adiciona mensagem de erro
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem.')
            return redirect('cadastro')
        
        # Verifica o comprimento da senha
        if len(senha) < 6:
            # Adiciona mensagem de erro
            messages.add_message(request, constants.ERROR, 'A senha deve ter pelo menos 6 caracteres.')
            return redirect('cadastro')
        
        try:
            # Cria o usuário com as informações fornecidas
            user = User.objects.create_user(
                first_name=primeiro_nome,
                last_name=ultimo_nome,
                username=username,
                email=email,
                password=senha,  # Aqui a senha será manipulada corretamente
            )
            # Após o registro, redireciona para a página de login ou uma página de sucesso
            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso!')
            return redirect('login')  # ou redirecionar para uma página de sucesso, se desejar
        except Exception as e:
            # Se ocorrer algum erro, adiciona uma mensagem de erro
            messages.add_message(request, constants.ERROR, 'Ocorreu um erro ao tentar criar o usuário. Tente novamente.')
            return redirect('cadastro')
        
        

def logar(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        # Verifique se o usuário existe e a senha está correta
        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)  # Faz o login do usuário na sessão
            return redirect('/')  # Redireciona para a página inicial após o login
        else:
            # Se as credenciais estiverem incorretas, exibe uma mensagem de erro
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return redirect('login')  # Redireciona de volta para a página de login

# Função 'home' movida para fora da função 'logar' para corrigir a indentação
def home(request):
    # Se o usuário estiver autenticado, passamos o nome dele para o template
    if request.user.is_authenticated:
        nome = request.user.first_name
        return render(request, 'home.html', {'nome': nome})
    
    return render(request, 'home.html')


def sair(request):
    logout(request)
    return redirect('/')
