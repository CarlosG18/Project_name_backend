from django import forms
from .models import Contato

class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['assunto'].widget.attrs.update({
            'class': 'assunto',
            'name': 'Assunto',
            'autocomplete': 'off',
        })
        
        self.fields['nome'].widget.attrs.update({
            'class': 'nome',
            'placeholder': "Nome",
            'autocomplete': 'off',
        })

        self.fields['email'].widget.attrs.update({
            'class': 'email',
            'placeholder': "Email",
            'autocomplete': 'off',
        })

        self.fields['mensagem'].widget.attrs.update({
            'class': 'mensagem',
            'placeholder': "Mensagem",
            'autocomplete': 'off',
        })