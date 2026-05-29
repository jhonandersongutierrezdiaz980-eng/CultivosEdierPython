from django import forms
from .models import Cultivo

class CultivoForm(forms.ModelForm):
    class Meta:
        model = Cultivo
        fields = ['nombre', 'agricultor', 'zona', 'cantidad_sembrada', 'observaciones']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'agricultor': forms.TextInput(attrs={'class': 'form-control'}),
            'zona': forms.Select(attrs={'class': 'form-select'}),
            'cantidad_sembrada': forms.NumberInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
