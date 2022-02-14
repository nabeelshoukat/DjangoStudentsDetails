from django.db import models

from django.contrib.auth.models import User

class BlogModel(models.Model):

    title =models.CharField(max_length=1000)
    
    slug=models.SlugField(max_length=1000)
    image=models.ImageField(upload_to='blog')
    create_at=models.DateTimeField(auto_now_add=True)
    upload_to=models.DateTimeField(auto_now=True)
class students(models.Model):
    first_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
