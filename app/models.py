from django.db import models


class Cidade(models.Model):
    nome = models.CharField(verbose_name="Cidade: ")
    UF = models.CharField(verbose_name="UF: ")
    def __str__(self):
        return f'{self.nome},{self.UF}'
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Usuarios(models.Model):
    nome = models.CharField(max_length=20, unique=True, verbose_name="Nome de usuário")
    telefone = models.CharField(max_length=60, verbose_name='Número de telefone do usuário')
    senha = models.CharField(max_length=128, verbose_name="Senha do usuário")
    dob = models.DateField(null=True, blank=True, verbose_name='Data de Nascimento') 
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name='E-mail') 
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True, verbose_name='Foto de Perfil')  

    def _str_(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

class Pais(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Viagens(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título da Viagem")
    descricao = models.TextField(verbose_name="Descrição da Viagem")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    imagem = models.ImageField(upload_to='imagens_viagens/', verbose_name="Imagem da Viagem", null=True, blank=True)
    data_disponibilidade = models.DateField(verbose_name="Data de Disponibilidade", null=True, blank=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, verbose_name="País", related_name="viagens")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Viagem"
        verbose_name_plural = "Viagens"
        ordering = ['titulo']

class TipoViagem(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome




class Profile(models.Model):
    user = models.OneToOneField(Usuarios, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='fotos_perfil/', default='default.jpg')

    def __str__(self):
        return self.user.nome 
    

