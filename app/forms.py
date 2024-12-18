from django import forms
from .models import *


class MensagemContatoForm(forms.ModelForm):
    class Meta:
        model = MensagemContato
        fields = ['nome', 'email', 'mensagem']
        
class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nome', 'email', 'comentario', 'estrelas']
        widgets = {
            'estrelas': forms.RadioSelect(),
        }