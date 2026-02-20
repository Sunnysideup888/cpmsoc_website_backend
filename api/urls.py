from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import hello_world, ItemViewSet, BlogItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'blog_items', BlogItemViewSet)

urlpatterns = [
    path('helloworld/', hello_world),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]