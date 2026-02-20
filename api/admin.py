from django.contrib import admin
from .models import Item, BlogItem

# Register your models here.
admin.site.register(Item)
admin.site.register(BlogItem)