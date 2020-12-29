from django.shortcuts import render,redirect
from recipes.forms import recipe_create_form
from django.views.generic import TemplateView
from recipes.models import Recipes
# Create your views here.

class RecipeCreate(TemplateView):
    model = Recipes
    template_name = "recipes/recipe_create.html"
    context = {}
    def get(self, request, *args, **kwargs):
        #user = self.model.objects.get(user=request.user)
        form = recipe_create_form(initial={"created_by":request.user})
        self.context["form"] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form = recipe_create_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            self.context["form"] = form
            return render(request,self.template_name,self.context)
class RecipeHome(TemplateView):
    template_name = "recipes/recipe_home.html"
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)
class ListMyRecipes(TemplateView):
    model = Recipes
    template_name = "recipes/myrecipes_list.html"
    context = {}
    def get(self, request, *args, **kwargs):
        my_recipes = self.model.objects.filter(created_by=request.user)
        self.context["recipes"] = my_recipes
        return render(request,self.template_name,self.context)
class EditMyRecipes(TemplateView):
    model = Recipes
    template_name = "recipes/edit_recipes.html"
    context = {}
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        recipe = self.model.objects.get(id=id)
        form = recipe_create_form(instance=recipe)
        self.context["form"] = form
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        recipe = self.model.objects.get(id=id)
        form = recipe_create_form(instance=recipe,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list")
        else:
            self.context["form"] = form
            return render(request,self.template_name,self.context)
        return render(request, self.template_name, self.context)
class ViewMyRecipe(TemplateView):
    model = Recipes
    template_name = "recipes/view_recipes.html"
    context = {}
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        recipe = self.model.objects.get(id=id)
        #form = recipe_create_form(instance=recipe)
        self.context["recipe"] = recipe
        return render(request,self.template_name,self.context)
class DeleteRecipe(TemplateView):
    model = Recipes
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        self.model.objects.get(id=id).delete()
        return redirect("list")
