from rest_framework import serializers
from .models import Item, BlogItem


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class BlogItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogItem
        fields = '__all__'

class BlogItemShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogItem
        exclude = ['text']