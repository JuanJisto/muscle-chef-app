from django.contrib import admin
from .models import Receta

# Esto hace que aparezca una tabla bonita en el panel de admin
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'proteinas', 'fecha_creacion')
    search_fields = ('titulo',)

admin.site.register(Receta, RecetaAdmin)