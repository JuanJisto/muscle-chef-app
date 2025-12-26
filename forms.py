from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'descripcion', 'ingredientes', 'proteinas', 'carbohidratos', 'grasas', 'imagen']
        
        # Aquí aplicamos "Tailwind CSS" a los inputs para que se vean modernos
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg', 'placeholder': 'Ej: Batido de Proteína'}),
            'descripcion': forms.Textarea(attrs={'class': 'w-full p-2 border rounded-lg', 'rows': 3}),
            'ingredientes': forms.Textarea(attrs={'class': 'w-full p-2 border rounded-lg', 'rows': 3}),
            'proteinas': forms.NumberInput(attrs={'class': 'w-1/3 p-2 border rounded-lg'}),
            # Puedes repetir el estilo para los demás campos
        }