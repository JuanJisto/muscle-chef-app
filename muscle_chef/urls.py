from django.contrib import admin
from django.urls import path, include  # <--- Fíjate que diga 'include' aquí
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # ESTA LÍNEA ES LA CLAVE: Le dice a Django "En la portada (''), carga las recetas"
    path('', include('recetas.urls')), 
    
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)