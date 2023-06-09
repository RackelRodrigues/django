from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
   name = models.CharField(max_length=65)



class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit= models.CharField(max_length=65)
    servings_unit = models.CharField(max_length=65)
    preparation_steps= models.TextField()
    preparetion_steps_is_html = models. BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_publish = models. BooleanField(default=False)
    cover = models.ImageField(upload_to='recepes/covers/%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="recipes")
