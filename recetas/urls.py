from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_recetas, name='lista_recetas'),
    path('receta/<int:id>/', views.detalle_receta, name='detalle_receta'),
    path('crear/', views.crear_receta, name='crear_receta'),
    
    path('receta/<int:id>/editar/', views.editar_receta, name='editar_receta'), 
]