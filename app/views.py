from pyexpat.errors import messages
from django.shortcuts import render,redirect
from .models import *
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required





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
            return redirect('viagens')
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
        foto_perfil = request.FILES.get('foto_perfil')  # Pega a foto do perfil, se enviada

        if senha != confirmar_senha:
            messages.error(request, "As senhas não conferem.")
            return render(request, 'criar_conta.html')
         
        usuario = Usuarios(nome=nome, telefone=telefone, dob=dob, email=email, senha=senha)


        if foto_perfil:
            usuario.foto_perfil = foto_perfil

        usuario.save()

 
        return redirect('/')


def viagens_view(request):
    viagens = Viagens.objects.all()
    return render(request, 'viagens.html', {'viagens': viagens})

@login_required
def perfil_view(request):
    return render(request, 'perfil.html', {'user': request.user})

@login_required
def editar_perfil_view(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)

        # Atualiza a imagem de perfil   
        if 'image' in request.FILES:
            user.profile.image = request.FILES['image']

        user.save()
        user.profile.save()
        messages.success(request, 'Perfil atualizado com sucesso!')
        return redirect('perfil')

    return render(request, 'editar_perfil.html', {'user': request.user})