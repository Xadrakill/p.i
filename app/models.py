from django.db import models



class Usuarios(models.Model):
    nome = models.CharField(max_length=20, unique=True, verbose_name="Nome de usuário")
    telefone = models.CharField(max_length=60, verbose_name='Número de telefone do usuário')
    senha = models.CharField(max_length=128, verbose_name="Senha do usuário")
    dob = models.DateField(null=True, blank=True, verbose_name='Data de Nascimento') 
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name='E-mail') 
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True, verbose_name='Foto de Perfil')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        
        
class Hotel(models.Model):
    nome = models.CharField(max_length=255)  # Nome do hotel
    descricao = models.TextField()  # Descrição do hotel
    endereco = models.CharField(max_length=255)  # Endereço do hotel
    cidade = models.CharField(max_length=100)  # Cidade onde o hotel está localizado
    estado = models.CharField(max_length=100)  # Estado
    foto_principal = models.ImageField(upload_to='hotels/', null=True, blank=True)  # Foto principal do hotel
    categoria = models.CharField(max_length=100, choices=[
        ('economico', 'Econômico'),
        ('luxo', 'Luxo'),
        ('medio', 'Médio'),
    ])  # Categoria do hotel

    # viagem = models.ForeignKey('Viagem', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
   
class Pais(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome do País")

    def __str__(self):
        return self.nome


    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Cidade")
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name="cidades", verbose_name="País")

    def __str__(self):
        return f"{self.nome} - {self.pais.nome}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Viagens(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título da Viagem")
    descricao = models.TextField(verbose_name="Descrição da Viagem")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    imagem = models.ImageField(upload_to='imagens_viagens/', verbose_name="Imagem da Viagem", null=True, blank=True)
    data_disponibilidade = models.DateField(verbose_name="Data de Disponibilidade", null=True, blank=True)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="País")
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Cidade")   
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Hotel")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Viagem"
        verbose_name_plural = "Viagens"
        ordering = ['titulo']

class MensagemContato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Certifique-se de que data_envio é do tipo DateTimeField
        if isinstance(self.data_envio, models.DateTimeField):
            return f"{self.nome} ({self.email}) - {self.data_envio.strftime('%d/%m/%Y %H:%M')}"
        return f"{self.nome} ({self.email})"
    
class Avaliacao(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField()
    estrelas = models.PositiveIntegerField(choices=[(i, f"{i} estrela{'s' if i > 1 else ''}") for i in range(1, 6)], default=5)
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.estrelas} estrelas"