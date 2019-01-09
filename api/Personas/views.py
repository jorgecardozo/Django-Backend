
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes

from .models import Personas
from .serializers import PersonasSerializer

from rest_framework import status
from rest_framework.response import Response
# Excepciones
from django.core.exceptions import ObjectDoesNotExist, FieldDoesNotExist
# Services
from .services.services import Exists 

#App Controller
from .controllers.controllers import Get, Create, Delete 
 
@api_view(['GET', 'POST'])
def _list(request):
    if request.method == "GET":
        #aca obtengo la lista
        data = PersonasSerializer(Personas.objects, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        #aca genero un nuevo elemento en la db
        serializer = PersonasSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        
        obj = Personas(**data)
        obj.save()

        reply = PersonasSerializer(obj).data

        return Response(reply, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE']) 
def _detail(request, id):
    if request.method == "GET":
        data = Get(id)
        return Response(data,status=status.HTTP_200_OK)
      
        #obtengo el elemento con id = id
    elif request.method == "PUT":
        pass
        # dto_serializer = PersonasSerializer(data=request.data, check_unique=False)
        # dto_serializer.is_valid(raise_exception=True)
        # data = dto_serializer.validated_data

        # obj = 
        #edito el elemento con id = id 

    elif request.method == "DELETE":
        Delete(id)
        return Response()
        #elimino el elemento con id = id 


