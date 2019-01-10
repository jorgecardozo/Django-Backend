from django.core.exceptions import ObjectDoesNotExist, FieldDoesNotExist
# from paradigma.objects.classes import DataTransferResultSet

from ..services.services import Exists
from ..serializers import PerroSerializer
from ..models import Perro
from rest_framework.response import Response

from django.db.models import F, Value
from django.db.models.functions import Concat
# metodos
def Get(id):
    if Exists(id):
        obj = Perro.objects.get(id=id)
        serializer = PerroSerializer(obj)
        return serializer.data
    else:
        raise ObjectDoesNotExist(id)
    
def Create(data):
    obj = Perro(**data)
    obj.full_clean()
    obj.save()
    return Get(obj.id)

def Edit(id, data):
    if Exists(id):
        obj = Perro.objects.get(id=id)
        for field, value in data.items():
            setattr(obj, field, value)
        obj.full_clean()
        obj.save()
        return Get(obj.id)
    else:
        raise ObjectDoesNotExist(id)

def Delete(id):
    if Exists(id):
        Perro.objects.get(id=id).delete()
        return Response()
    else:
        raise ObjectDoesNotExist(id)