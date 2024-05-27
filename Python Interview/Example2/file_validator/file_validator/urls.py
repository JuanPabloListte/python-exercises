from django.contrib import admin
from django.urls import path
from django.urls.conf import include

# Se importa la vista de validación de archivos a la ruta principal
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]
