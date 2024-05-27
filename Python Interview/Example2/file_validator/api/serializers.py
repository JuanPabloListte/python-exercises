from rest_framework import serializers

# Se crea el serializador para la validación de archivos, este recibe una lista de archivos y los serializa
class ValdiationFileSerializer(serializers.Serializer):
    file_names = serializers.ListField(
        child=serializers.CharField(max_length=100)
    )