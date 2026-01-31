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

# All the other routes are handled by Django already so like regular GET, PUT, POST, DELETE
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

    # GET /api/blog_items/by_slug/{slug}/
    @action(detail=False, methods=['get'], url_path='by_slug/(?P<slug>[^/.]+)')
    def by_slug(self, request, slug=None):
        blog = get_object_or_404(BlogItem, slug=slug)
        serializer = BlogItemSerializer(blog)
        return Response(serializer.data)

    # GET /api/blog_items/filter_by_tags/
    # Use it kind of like this /?tags=Mathematics&tags=Computer Science"
    # Note that you shouldn't have to deal with adding %20 or anything it'll do it itself
    @action(detail=False, methods=['get'], url_path='filter_by_tags')
    def filter_by_tags(self, request):
        tags_list = request.query_params.getlist('tags')

        if not tags_list:
            return Response(
                {"error": "No tags provided!!!"},
                status=400
            )

        blogs = self.get_queryset().filter(tags__contains=tags_list)
        serializer = BlogItemShortSerializer(blogs, many=True)
        return Response(serializer.data)

    # GET /api/blog_items/get_next_by_slug/{SLUG}
    @action(detail=False, methods=['get'], url_path='get_next_by_slug/(?P<slug>[^/.]+)')
    def get_next_by_slug(self, request, slug=None):
        current_blog = get_object_or_404(BlogItem, slug=slug)

        next_blog = BlogItem.objects.filter(
            date_published__lt=current_blog.date_published
        ).order_by('-date_published').first()

        if not next_blog:
            next_blog = BlogItem.objects.order_by('-date_published').first()

        serializer = BlogItemShortSerializer(next_blog)
        return Response(serializer.data)