from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import hello_world, ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('helloworld/', hello_world),
    path('', include(router.urls)),
]