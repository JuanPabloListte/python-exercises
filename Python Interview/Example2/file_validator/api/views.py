# api/views.py
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import ValdiationFileSerializer
import os
from datetime import datetime

class ValidateFilesView(APIView):
    # Se definen los parsers que se van a utilizar en la vista para poder recibir archivos y JSON
    parser_classes = [MultiPartParser, JSONParser]

    # Se define el método POST para la vista, este recibe una lista de archivos
    def post(self, request, *args, **kwargs):
        # data recibe la data que se envía en la petición y la serializa
        data = request.data
        serializer = ValdiationFileSerializer(data=data)

        # si el serializador es válido, se obtienen los nombres de los archivos
        if serializer.is_valid():
            file_names = serializer.validated_data['file_names']
            response = []

            # Se recorre la lista de archivos obtenidos
            for file_name in file_names:
                # Se obtiene la ruta del archivo
                file_path = os.path.join(settings.FILES_DIR, file_name)
                # si la ruta existe se obtiene la fecha de modificación del archivo y se agrega a la respuesta
                if os.path.exists(file_path):
                    last_modified_time = os.path.getmtime(file_path)
                    last_modified_date = datetime.fromtimestamp(last_modified_time).isoformat()
                    response.append({
                        'file_name': file_name,
                        'last_modified': last_modified_date
                    })
                else:
                    # si no se encuentra se devuelve un error
                    response.append({
                        'file_name': file_name,
                        'error': 'File does not exist'
                    })

            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
