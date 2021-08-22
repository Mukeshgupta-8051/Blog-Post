from django.db import models

# Create your models here.
class Blog(models.Model):
    bloger = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    postdate = models.DateTimeField(auto_now_add=True)
    post = models.CharField(max_length=255)