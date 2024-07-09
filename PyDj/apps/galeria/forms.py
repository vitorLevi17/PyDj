from .models import Fotografia
from django import forms

class FotografiaForms(forms.ModelForm):
    class Meta: ##referencia a metadados de fotografia
        model = Fotografia
        exclude = ['publicada']
        labels = {
            'descricao':'Descrição',
            'datas':'Data da foto',
            'usu':'Usuário'
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'})
            ,'legenda':forms.TextInput(attrs={'class':'form-control'})
            ,'categoria':forms.Select(attrs={'class':'form-control'}),
            'descricao':forms.Textarea(attrs={'class':'form-control'}),
            'foto':forms.FileInput(attrs={'class':'form-control'}),
            'datas':forms.DateTimeInput(
                format='%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'}),
            'usu':forms.Select(attrs={'class':'form-control'})
        }

