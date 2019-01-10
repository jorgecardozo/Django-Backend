
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes

from .models import Perro
from .serializers import PerroSerializer

from rest_framework import status
from rest_framework.response import Response
# Excepciones
from django.core.exceptions import ObjectDoesNotExist, FieldDoesNotExist
# Services
from .services.services import Exists 

#App Controller
from .controllers.controllers import Get, Create, Delete, Edit
 
@api_view(['GET', 'POST'])
def _listP(request):
    if request.method == "GET":
        #aca obtengo la lista
        data = PerroSerializer(Perro.objects, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        #aca genero un nuevo elemento en la db
        serializer = PerroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data    
        
        obj = Perro(**data)
        obj.save()

        reply = PerroSerializer(obj).data

        return Response(reply, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE']) 
def _detailP(request, id):
    if request.method == "GET":
        data = Get(id)
        return Response(data,status=status.HTTP_200_OK)
      
        #obtengo el elemento con id = id
    elif request.method == "PUT":
        serializer = PerroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        obj_result = Edit(id, data)

        return Response()
        # obj = 
        #edito el elemento con id = id 

    elif request.method == "DELETE":
        Delete(id)
        return Response()
        #elimino el elemento con id = id 
