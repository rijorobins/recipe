from django.db import models

# Create your models here.

class Recipes(models.Model):
    recipe_name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=500)
    category = models.CharField(max_length=100)
    recipe_image = models.ImageField(upload_to="images")
    created_by = models.CharField(max_length=100)
    def __str__(self):
        return self.recipe_name

