from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

# This is for all the blog items
class BlogItem(models.Model):
    blog_name = models.CharField(max_length=200, unique=True)
    date_published = models.DateField()
    author = models.CharField(max_length=100)
    tldr_text = models.TextField()
    tags = models.JSONField(default=list)
    tile_image = models.URLField()
    blog_image = models.URLField()
    text = models.TextField()

    def __str__(self):
        return self.blog_name