from django.http import JsonResponse
from .models import Server
from  .serializers import ServerSerializer


def server_list(request):
    servers = Server.objects.all()
    serializer = ServerSerializer(servers,many=True)
    return JsonResponse(serializer.data, safe=False)
    