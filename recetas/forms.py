from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'descripcion', 'ingredientes', 'proteinas', 'carbohidratos', 'grasas', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'Ej: Pollo con Arroz'}),
            'descripcion': forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'rows': 2}),
            'ingredientes': forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'rows': 2}),
        }