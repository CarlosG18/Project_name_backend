from django import forms
from .models import Contato

class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        fields = "__all__"

