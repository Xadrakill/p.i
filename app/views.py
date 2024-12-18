from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import *




class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidades.html', {'cidades':
cidades})
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Usuarios.objects.get(nome=username)
        except Usuarios.DoesNotExist:
            messages.error(request, 'Usuário inexistente')
            return render(request, 'index.html')

        if password == user.senha:
            request.session['user_id'] = user.id  
            return redirect('inicio')
        else:
            messages.error(request, 'Usuário ou senha incorretos')

    return render(request, 'index.html')

class CriarContaView(View):
    def get(self, request):
        return render(request, 'criar_conta.html')
    
    def post(self, request):
        nome = request.POST['username']
        telefone = request.POST['telefone']
        dob = request.POST['dob']
        email = request.POST['email']
        senha = request.POST['password']
        confirmar_senha = request.POST['confirm_password']
        foto_perfil = request.FILES.get('foto_perfil')

        # Validação de senhas
        if senha != confirmar_senha:
            messages.error(request, "As senhas não conferem.")  # Adiciona mensagem de erro
            return redirect('/criar-conta/')

        # Verifica se o email já existe
        if Usuarios.objects.filter(email=email).exists():
            messages.error(request, "Este email já está cadastrado.")  # Adiciona mensagem de erro
            return redirect('/criar-conta/')

        # Criação do novo usuário
        usuario = Usuarios(nome=nome, telefone=telefone, dob=dob, email=email, senha=senha)
        
        if foto_perfil:
            usuario.foto_perfil = foto_perfil  # Salva a foto de perfil, se enviada

        usuario.save()
        messages.success(request, "Conta criada com sucesso! Faça login.")  # Adiciona mensagem de sucesso
        return redirect('/')


def viagens_view(request):
    viagens = Viagens.objects.all()
    return render(request, 'viagens.html', {'viagens': viagens})


def comprar_viagem(request, id):
    try:
        viagem = Viagens.objects.get(id=id)
    except Viagens.DoesNotExist:
        return render(request, '404.html', {})  # Ou redirecionar para uma página de erro adequada.

    return render(request, 'comprar.html', {'viagem': viagem})



def explorar_viagens(request):
    pais_selecionado = request.GET.get('pais', None)
    paises = Pais.objects.all()  # Lista de todos os países para o dropdown

    if pais_selecionado:
        viagens = Viagens.objects.filter(pais__nome=pais_selecionado)
    else:
        viagens = Viagens.objects.all()

    context = {
        'viagens': viagens,
        'paises': paises,
        'pais_selecionado': pais_selecionado,
    }
    return render(request, 'viagens.html', context)


def inicio(request):
    return render(request, 'inicio.html')


def contato_view(request):
    if request.method == 'POST':
        form = MensagemContatoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva a mensagem no banco de dados
            return JsonResponse({'status': 'sucesso'})
        return JsonResponse({'status': 'erro', 'erros': form.errors})

    return render(request, 'contato.html', {})

def avaliacao_view(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'sucesso'})
        return JsonResponse({'status': 'erro', 'erros': form.errors})

    # Recuperar todas as avaliações existentes
    avaliacoes = Avaliacao.objects.order_by('-data_envio')
    form = AvaliacaoForm()
    return render(request, 'avaliacoes.html', {'form': form, 'avaliacoes': avaliacoes})