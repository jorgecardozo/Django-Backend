from ..models import Perro

def Exists(id):
    """
    Devuelve True o Falso de acuerdo a si existe o no.
    """
    return Perro.objects.filter(id=id).exists()