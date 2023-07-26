from django.http import JsonResponse
from .models import Server
from  .serializers import ServerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(('GET','POST',))
def server_list(request):
    if request.method == 'GET':
        servers = Server.objects.all()
        serializer = ServerSerializer(servers,many=True)
        return JsonResponse({'servers':serializer.data})

    if request.method == 'POST':
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    