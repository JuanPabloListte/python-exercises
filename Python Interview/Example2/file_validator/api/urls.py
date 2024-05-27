from django.urls import path
from .views import ValidateFilesView

# Ruta para la vista de validación de archivos
urlpatterns = [
    path('validate/', ValidateFilesView.as_view(), name='validate')
]