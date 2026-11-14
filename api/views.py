from .serializers import RegistroSerializer, UserSerializer
from .models import Registro, User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def registro_list(request):
    registros = Registro.objects.all()
    serializer = RegistroSerializer(registros,many=True)
    return Response(serializer.data)



@api_view(['GET'])
def usuario_list(request):
    usuarios = User.objects.all()
    serializer = UserSerializer(usuarios,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def usuario_detail(request,pk):
    usuario = get_object_or_404(User,pk=pk)
    serializer = UserSerializer(usuario)
    return Response(serializer.data)

