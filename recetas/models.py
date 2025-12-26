from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    ingredientes = models.TextField(help_text="Separa ingredientes por comas")
    proteinas = models.DecimalField(max_digits=5, decimal_places=1)
    carbohidratos = models.DecimalField(max_digits=5, decimal_places=1)
    grasas = models.DecimalField(max_digits=5, decimal_places=1)
    imagen = models.ImageField(upload_to='recetas/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
