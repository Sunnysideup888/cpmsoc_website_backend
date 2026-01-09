from rest_framework import viewsets
from django.http import JsonResponse
from .models import Item
from .serializers import ItemSerializer

def hello_world(request):
    return JsonResponse({"message": "Hello World"})

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer