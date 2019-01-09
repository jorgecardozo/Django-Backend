from django.core.exceptions import ObjectDoesNotExist, FieldDoesNotExist
from ..services.services import Exists
from ..serializers import PersonasSerializer
from ..models import Personas
from rest_framework.response import Response

def Get(id,):
    if Exists(id):
        obj = Personas.objects.get(id=id)
        serializer = PersonasSerializer(obj)
        return serializer.data
    else:
        raise ObjectDoesNotExist(id)
    
def Create(data):
    obj = Personas(**data)
    obj.full_clean()
    obj.save()
    return Get(obj.id)

# def Edit(id, data):
#     if Exists(id):
#         obj = Personas.objects.get(id=id)
#         for field, value in data.items():
#             setattr(obj, field, value)
#         obj.full_clean()
#         obj.save()
#         return Get(obj.id)
#     else:
#         raise ObjectDoesNotExist(id)

def Delete(id):
    if Exists(id):
        Personas.objects.get(id=id).delete()
        return Response()
    else:
        raise ObjectDoesNotExist(id)