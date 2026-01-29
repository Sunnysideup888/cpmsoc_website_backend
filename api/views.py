from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Item, BlogItem
from .serializers import ItemSerializer, BlogItemSerializer, BlogItemShortSerializer


def hello_world(request):
    return JsonResponse({"message": "Hello World"})

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# All the other routes are handled by Django already
class BlogItemViewSet(viewsets.ModelViewSet):
    queryset = BlogItem.objects.all().order_by('-date_published')
    serializer_class = BlogItemSerializer
    lookup_field = 'id'

    # GET /api/blog_items/shortened/
    @action(detail=False, methods=['get'])
    def shortened(self, request):
        blogs = self.get_queryset()
        serializer = BlogItemShortSerializer(blogs, many=True)
        return Response(serializer.data)

    # GET /api/blog_items/by_name/{blog_name}/
    @action(detail=False, methods=['get'], url_path='by_name/(?P<blog_name>[^/.]+)')
    def by_name(self, request, blog_name=None):
        blog = get_object_or_404(BlogItem, blog_name=blog_name)
        serializer = BlogItemSerializer(blog)
        return Response(serializer.data)