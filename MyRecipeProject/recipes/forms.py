from django.forms import ModelForm
from django import forms
from recipes.models import Recipes

class recipe_create_form(ModelForm):
    ingredients = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Recipes
        fields = ["recipe_name","ingredients","category","recipe_image","created_by"]
