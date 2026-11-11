from django.http import JsonResponse
from .serializers import RegistroSerializer
from .models import Registro



def registro_list(request):
    registros = Registro.objects.all()
    serializer = RegistroSerializer(registros,many=True)
    return JsonResponse({
        'data':serializer.data,
    })
